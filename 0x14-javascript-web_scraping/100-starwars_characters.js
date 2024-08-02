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
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (error, response, body) => {
        if (error) {
          console.error(error);
        }
        if (response.statusCode === 200) {
          const people = JSON.parse(body);
          const person = people.name;
          console.log(person);
        }
      });
    }
  }
});
