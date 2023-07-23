const randomTestButton = document.getElementById("random-test-button");

const idTestButton = document.getElementById("id-test-button");
const idEntry = document.getElementById("id-input");

function GetRandomJoke() {
  fetch("/random")
    .then((response) => response.json())
    .then((data) => {
      var randomCodeBlock = document.getElementById("get-random-code-block");
      randomCodeBlock.innerHTML = `{\n\tid: ${data["id"]}\n\tjoke: ${data["main_joke"]}\n}`;
    })
    .catch((error) => console.error(error));
}

function GetIdJoke() {
  let id = idEntry.value;
  fetch(`/id/${id}`)
    .then((response) => response.json())
    .then((data) => {
      var idCodeBlock = document.getElementById("get-by-id-code-block");
      idCodeBlock.innerHTML = `{\n\tid: ${data["id"]}\n\tjoke: ${data["main_joke"]}\n}`;
    })
    .catch((error) => console.error(error));
}

randomTestButton.addEventListener("click", GetRandomJoke);
idTestButton.addEventListener("click", GetIdJoke);
