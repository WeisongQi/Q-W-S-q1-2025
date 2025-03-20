let zufallszahl = Math.floor(Math.random() * 10) + 1;
console.log(zufallszahl);
checkGuess = () => {
    let eingabe = document.getElementById("guess").value;
    if (eingabe == zufallszahl) {
        alert("Super! Richtig geraten!");
    } else if (eingabe < zufallszahl) {
        alert("Leider es ist zu klein. nochmal versuchen!");
    } else {
        alert("Leider es ist zu groß. nochmal versuchen!");
    }
}