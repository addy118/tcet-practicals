const http = require('http');
const fs = require('fs');
const path = require('path');


const hostname = '127.0.0.1';
const port = 3000;
const usersFilePath = path.join(__dirname, 'users.json');


const server = http.createServer((req, res) => {
    if (req.method === 'POST' && req.url === '/registerUser') {
        let body = '';


        req.on('data', chunk => body += chunk.toString());
        req.on('end', () => {
            try {
                const user = JSON.parse(body);
                if (!user.name || !user.email) {
                    res.statusCode = 400;
                    res.end('Missing name or email');
                    return;
                }


                fs.readFile(usersFilePath, 'utf8', (err, data) => {
                    if (err) {
                        res.statusCode = 500;
                        res.end('Error reading users file');
                        return;
                    }


                    const users = JSON.parse(data || '[]');
                    user.id = users.length ? users[users.length - 1].id + 1 : 1; // Auto-increment ID
                    users.push(user);


                    fs.writeFile(usersFilePath, JSON.stringify(users, null, 2), err => {
                        if (err) {
                            res.statusCode = 500;
                            res.end('Error writing users file');
                            return;
                        }
                        res.statusCode = 201;
                        res.end('User registered');
                    });
                });
            } catch {
                res.statusCode = 400;
                res.end('Invalid JSON');
            }
        });


    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});


server.listen(port, hostname, () => {
    console.log("Server running at http://${hostname}:${port}/");
});