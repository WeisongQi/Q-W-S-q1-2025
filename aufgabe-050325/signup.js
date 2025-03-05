function onClickButton() {
  const boxDiv = document.getElementById("box");
  boxDiv.innerHTML = "<button>Im a button</button>";
  const currentBgColor = boxDiv.style.backgroundColor;
  console.log("box div background", currentBgColor);
  boxDiv.style.backgroundColor = "green";
}

function onSignup() {
  const emailTI = document.getElementById("emailti").value;
  const password = document.getElementById("passwordti").value;
  const passwordRT = document.getElementById("passwordrt").value;
  const firstname = document.getElementById("firstname").value;
  const lastname = document.getElementById("lastname").value;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  console.log("My Credentials", emailTI, password);
  if (passwordRT.length == 0 &&
     emailTI.length == 0 &&
     firstname.length == 0 &&
     lastname.length == 0 &&
     password.length == 0) {
    alert(
      "Bitte füllen Sie alle Felder aus"
      );
    return;
  }
  if (password !== passwordRT) {
    alert("Die Passwörter stimmen nicht überein");
    return;
  }
  if (!emailRegex.test(emailTI)) {
    alert("Die Email ist nicht korrekt");
    return;
  }

  alert(
    `Der Bneutzer ${firstname} ${lastname} hat sich erflogreich mit ${emailTI} und ${password} angemeldet`
    );
}
