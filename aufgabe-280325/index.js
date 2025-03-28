const express = require('express')
const app = express()
const fs = require('fs')
const port = 5050
app.use(express.json())

function readData() {

    const data = fs.readFileSync('produkteList.json', 'utf8');
    return JSON.parse(data);

}

function writeData(data) {
    fs.writeFileSync('produkteList.json', JSON.stringify(data, null, 2));
}

app.get("/produkte", (req, res) => {
    const products = readData();
    res.json(products);
})

app.get("/produkte/search", (req, res) => {
    const products = readData();
    const sorten = req.query.sorten;
    const name = req.query.name;
    const art = req.query.art;
    const foundProdukte = products.filter(product => {
        let match = true;
        if (sorten !== undefined && product.sorten !== sorten) { match = false; }
        if (name !== undefined && product.name !== name) { match = false; }
        if (art !== undefined && product.art !== art) { match = false; }
        return match;
    });
    res.status(202).json(foundProdukte);
})

app.post("/produkte", (req, res) => {
    const products = readData();
    const { name, sorten, art } = req.body
    if (name && sorten && art) {
        const newProdukte = {
            id: products.length + 1,
            name: name,
            sorten: sorten,
            art: art
        }
        products.push(newProdukte)
        writeData(products)
        res.status(201).json(newProdukte)
    }
    else { res.send("Daten falsch!") }

})
app.put("/produkte/:id", (req, res) => {
    const id = req.params.id;
    const products = readData();
    const newName = req.body.name;
    const newSorten = req.body.sorten;
    const newArt = req.body.art;
    const up_Producte = products.find(product => product.id == id);
    up_Producte.name = newName;
    up_Producte.sorten = newSorten;
    up_Producte.art = newArt;
    res.json(up_Producte);
    writeData(products);
})

app.delete("/produkte/:id", (req, res) => {
    const id = req.params.id;
    const products = readData();
    const index = products.findIndex(product => product.id == id);
    const delProducte = products.splice(index, 1);
    if (!id || isNaN(id)) {
        res.status(400).json({ error: "ID cannot be empty or invalid" });
        return;
    }

    writeData(products);
    res.json("Produkte gelöscht: " + delProducte[0].name);

})

app.listen(port)
