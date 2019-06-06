var http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('HelloWorld');
}).listen(8080);

/* Open browser: http://localhost:8080 */