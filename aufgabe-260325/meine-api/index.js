const express = require('express');
const app = express();
let generateName = require('sillyname');
let sillyName = generateName();

app.get('/', (req, res) => {
    res.send("Welcome to my API");
});

app.get("/data", (req, res) => {
    res.json([
        { id: 1, name: "Max" },
        { id: 2, name: "Lena" }
    ]);
});

app.get("/randomname", (req, res) => {
    res.send("Random Name: " + sillyName);
});

app.route('/book')
    .get((req, res) => {
        res.send('Get a ' + sillyName + ' book')
    })
    .post((req, res) => {
        res.send('Add a book')
    })
    .put((req, res) => {
        res.send('Update the book')
    })

app.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
});
