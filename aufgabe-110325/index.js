const express = require('express'); // 如果使用 CommonJS
// import express from 'express'; // 如果使用 ES Module

const app = express();

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

app.get('/', (req, res) => {
    res.send('Hello world!');
});

app.get('/content', (req, res) => {
    res.send('<h1>Welcome to My Page!</h1><p>This is an awesome HTML content.</p>');
});

app.get('/api/data', (req, res) => {
    res.json({ fullName: 'Lukas Probst', age: 28 });
});
