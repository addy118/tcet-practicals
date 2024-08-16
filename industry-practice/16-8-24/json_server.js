var http = require("http");
http.createServer(function (req, res) {
    res.writeHead(200, { "Content-Type": "application/json" })
    var data = {
        "name": "Aditya",
        "email": "addyyy118@gmail.com"
    }
    res.write(JSON.stringify(data))
    res.end("\nHello World!")
}).listen(8081)

console.log('Server listening on http://127.0.0.1:8081')