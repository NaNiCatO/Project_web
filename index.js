const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
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

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
