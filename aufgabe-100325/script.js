// my_list soll auf der Website dargestellt werden
let my_list = []

// createHTMLList nimmt ein Javascript Array und gibt einen String für eine
// ungeordnete HTML Liste zurück
function createHTMLList(liste) {

    let htmlElements = liste.map((listItem) => `<li>${listItem}</li>`)
    //console.log(htmlElements)
    let flattenedList = htmlElements.join("")
    //console.log(flattenedList)
    let ergebnis = `<ul>${flattenedList}</ul>`
    return ergebnis
}

// setListContent setzt den Inhalt des "liste"-div auf das Ergebnis eines createHTMLList(my_list) Aufrufs
function setListContent() {
    let listDiv = document.getElementById("liste")
    let content = createHTMLList(my_list)
    listDiv.innerHTML = content
}

// setUserInputList liest das eingabefeld und rendered die liste daraus
// text = "Lukas, Christof, Mete, Wojciech"
function setUserInputList() {
    //Erstmal Text und div aus dem Dokument holen
    let userInput = document.getElementById("userInput")
    let text = userInput.value
    let textList = text.split(",")
    my_list = my_list.concat(textList)
    setListContent()
}

// addSingleItem liest das Einzelneingabefeld und fügt das Element zur Liste hinzu
function addSingleItem() {
    let singleInput = document.getElementById("singleInput")
    let item = singleInput.value
    if (item) {
        my_list.push(item)
        setListContent()
    }
}

// removeLastItem entfernt das letzte Element aus der Liste
function removeLastItem() {
    my_list.pop()
    setListContent()
}

// removeItemByIndex entfernt das Element an der angegebenen Position aus der Liste
function removeItemByIndex(index) {
    if (index >= 0 && index < my_list.length) {
        my_list.splice(index, 1);
        setListContent();
    }
}

// changeColor ändert die Farben der Blöcke und aller Buttons
function changeColor() {
    const block1 = document.getElementById('block1');
    const block3 = document.getElementById('block3');
    const buttons = document.querySelectorAll('button');
    let tempColor = block3.style.backgroundColor;

    block1.style.backgroundColor = 'blue';
    block3.style.backgroundColor = 'red';
    buttons.forEach(button => button.style.backgroundColor = 'green');

    setTimeout(() => {
        block1.style.backgroundColor = tempColor;
        block3.style.backgroundColor = tempColor;
        buttons.forEach(button => button.style.backgroundColor = '');
    }, 1000);
}
