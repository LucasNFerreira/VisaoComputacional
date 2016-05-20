var http = require('http');
var fs = require('fs');

http.createServer(function ( req, res ) { // req = requisição, res = resposta

    

    // Leia o conteúdo do arquivo para a memória
    fs.readFile('teste.txt', function ( err, logData ) {

    // Se um erro ocorrer, será lançada uma
    // exceção, e a aplicação irá ser encerrada
    if ( err ) throw err;

    // logData é um Buffer, converta-o para string
    var text = logData.toString();

    res.writeHead( 200, { 'Content-Type': 'text/plain' } );
    res.end( text);
})
}).listen( 8080 );

console.log( 'Servidor rodando na porta 8080' );