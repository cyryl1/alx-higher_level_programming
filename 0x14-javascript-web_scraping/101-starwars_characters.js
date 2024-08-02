#!/usr/bin/node

const request = require('request');

const args = process.argv;
const movieId = args[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    const printCharacter = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }

          if (response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
            resolve();
          } else {
            reject(new Error(`Failed to fetch character: ${response.statusCode}`));
          }
        });
      });
    };

    let promise = Promise.resolve();
    characters.forEach(charUrl => {
      promise = promise.then(() => printCharacter(charUrl));
    });

    promise.catch(error => console.error(error));
  } else {
    console.error(`Failed to fetch movie: ${response.statusCode}`);
  }
});
