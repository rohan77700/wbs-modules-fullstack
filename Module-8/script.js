const randomizeButton = document.getElementById('randomize-button');
const characterInfo = document.querySelector('.character-info');
const pokeName = document.querySelector('.name');
const description = document.querySelector('.description');
const image = document.querySelector('.image');

randomizeButton.addEventListener('click', getRandomCharacter);
    function getRandomCharacter() {
        const url = 'https://pokeapi.co/api/v2/pokemon/' + Math.floor(Math.random() * 1302) + '/';

        fetch(url)
            .then(response => response.json())
            .then(data => {
                pokeName.textContent = data.name;
                description.textContent = `Ability: ${data.abilities[0].ability.name}, Height: ${data.height} cm, Weight: ${data.weight} kg`;
                image.src = data.sprites.front_default;
            });
    }

getRandomCharacter();