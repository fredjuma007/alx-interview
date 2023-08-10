#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
    const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

    request(movieUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }

        if (response.statusCode !== 200) {
            console.error('API Error:', response.statusCode, body);
            return;
        }

        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;
        
        characterUrls.forEach(characterUrl => {
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Character Error:', charError);
                    return;
                }

                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
            });
        });
    });
}

const movieId = process.argv[2];
if (!movieId) {
    console.log('Usage: node script.js <movieId>');
    process.exit(1);
}

getMovieCharacters(movieId);

