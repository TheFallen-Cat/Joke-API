const randomTestButton = document.getElementById('random_test_button');

const idTestButton = document.getElementById('id_test_button');
const idEntry = document.getElementById('id_input');


function GetRandomJoke() {
    // var hljs = window.hljs;

    fetch('/api/random')
        .then(response => response.json())
        .then(data => {
            var randomCodeBlock = document.getElementById('get_random_code_block');
            randomCodeBlock.innerHTML = `{\n\tid: ${data['id']}\n\tjoke: ${data['main_joke']}\n}`;
        })
        .catch(error => console.error(error));
}

function GetIdJoke() {

    let id = idEntry.value;
    fetch(`/api/id/${id}`)
        .then(response => response.json())
        .then(data => {
            var idCodeBlock = document.getElementById('get_by_id_code_block');
            idCodeBlock.innerHTML = `{\n\tid: ${data['id']}\n\tjoke: ${data['main_joke']}\n}`;
        })
        .catch(error => console.error(error));
}

randomTestButton.addEventListener('click', GetRandomJoke)
idTestButton.addEventListener('click', GetIdJoke)

