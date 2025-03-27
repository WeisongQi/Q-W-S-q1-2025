const express = require('express');
const fs = require('fs');
const app = express();

const filePath = './jsonDateBooks/bookOutput.json';
app.use(express.json());

const bookList = [
    { id: 1, title: "Harry Potter", author: "J.K. Rowling" },
    { id: 2, title: "Der Herr der Ringe", author: "J.R.R. Tolkien" },
    { id: 3, title: "Der kleine Prinz", author: "Antoine de Saint-Exupéry" },
    { id: 4, title: "Mathematik für Informatiker", author: "Gerald Teschl" },
    { id: 5, title: "Logik für Informatiker", author: "Uwe Schöning" },
];
const jsonDate = JSON.stringify(bookList, null, 2);

app.get("/books", (req, res) => {
    res.json(bookList);
});

// Search route must be defined before the idfind route
// `/books/search` 路由必须在 `/books/:id` 路由之前定义
app.get("/books/search", (req, res) => {
    const title = req.query.title;
    const foundBook_t = bookList.filter(book => book.title == title);
    if (foundBook_t) {
        res.json(foundBook_t);
    } else {
        res.status(404).send("Book not found");
    }
});

// idfind route
app.get("/books/:id", (req, res) => {
    const id = req.params.id;
    const foundBook = bookList.find(book => book.id == id);
    if (foundBook) {
        res.json(foundBook);
    } else {
        res.status(404).send("Book not found");
    }
});

app.post("/books", (req, res) => {
    const { title, author } = req.body;
    const newBook = {
        id: bookList.length + 1,
        title: title,
        author: author,
    };
    bookList.push(newBook);
    res.json(bookList);
})

fs.writeFileSync(filePath, jsonDate, 'utf8');
app.listen(5400);