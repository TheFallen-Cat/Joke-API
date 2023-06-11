const randomButton = document.getElementById('random_joke_button');
const jokeText = document.getElementById('joketext');

function showRandomJoke() {

    fetch('/get/random')
        .then(response => response.json())
        .then(data => { jokeText.innerText = data['main_joke']; })

        .catch(error => { console.log(error); })
}

randomButton.addEventListener('click', showRandomJoke)
document.addEventListener('DOMContentLoaded', showRandomJoke)