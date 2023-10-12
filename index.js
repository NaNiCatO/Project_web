const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const http = require('http');
const socketIo = require('socket.io');


const app = express();
const server = http.createServer(app);
const io = socketIo(server);
const port = process.env.PORT || 8000;


app.use(express.static(path.join(__dirname)));
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'page', 'login.html'));
});


app.post('/process_login', (req, res) => {
    const { username, password } = req.body;

    // Here, you can perform authentication and other logic.
    // Replace this with your actual authentication code.
    if (username === 'name' && password === 'pass') {
        res.sendFile(path.join(__dirname, 'page', 'channel.html'));
    } else {
        res.status(401).json({ message: 'Login failed' });
    }
});


app.get('/join_meeting', (req, res) => {
    res.sendFile(path.join(__dirname, 'page', 'meeting.html'));
});


io.on('connection', (socket) => {
    console.log('A user has connected');

    // Handle WebRTC signaling and user interaction here

    socket.on('disconnect', () => {
        // Handle user disconnection
    });
});


app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
