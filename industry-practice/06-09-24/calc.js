/*
CW: Create new api calc.js

Create API with 4 methods:
add => GET | I am from addition
sub => POST | I am from subtraction
mul => PUT | I am from multiplication
div => DELETE | I am from division
*/

app.get("/sqr", (req, res) => {
    x = 5;
    result = `Square of ${x} is ${x * x}`
    res.send(result)
})

