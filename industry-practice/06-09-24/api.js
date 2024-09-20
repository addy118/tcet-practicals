var express = require('express')
// npm i express

var app = express();
const PORT = 8989

app.get("/", (req, res) => {
    res.send("Hello from Aditya Kirti");
})

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`)
})