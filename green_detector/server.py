#!/usr/bin/env python

from twisted.web import server 
from twisted.web import resource
from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.static import File
import json
import GraphData
import detector as dtc
import threading
import webbrowser

data = GraphData.GraphData([])
dataGraph = 'data'

class Counter(resource.Resource):
    isLeaf = True
    numberRequests = 0
    def render_GET(self, request):
        self.numberRequests += 1
        if(request.uri == '/json'):
            request.setHeader(b"content-type", b"application/json")
            content = json.dumps({dataGraph: data.values[-1][1]})
            return content
        elif(request.uri == '/chart' or request.uri == "/"):
            file = open('mean/index.html')
            content = file.read()
            file.close()
            return content

        elif(request.uri == '/css/chart.css'):
            file = open('mean/css/chart.css')
            content = file.read()
            file.close()
            return content
        
        else:
            print request.uri
            return "this page is not avaliable"


def runServer(x):
    root = Counter()
    root.putChild('json', File(json.dumps({dataGraph: data.values})))
    root.putChild('graph', File('mean/'))
    endpoints.serverFromString(reactor, "tcp:8000").listen(server.Site(root))
    reactor.run()

def runInParallel():
	t1 = threading.Thread(target = runServer, args = (0,))
	t1.start()

	t2 = threading.Thread(target = dtc.run, args = (data,))
	t2.start()

runInParallel()
webbrowser.open('http://127.0.0.1:8000')