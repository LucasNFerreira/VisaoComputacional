var fs = require('fs');

var data

fs.readFile('teste.json', function(err,data){
    if(err) {
        console.error("Could not open file: %s", err);
        process.exit(1);
    }
    
    var http = require('http');
  	http.createServer(function (req, res) {
    		res.setHeader('Content-Type', 'application/json');
        var jsonContent = JSON.parse(data);
    		res.end(JSON.stringify(jsonContent), null, 3);
  	}).listen(3000);
  	console.log('Server running at http://localhost:8080/');

    console.log(data);
});