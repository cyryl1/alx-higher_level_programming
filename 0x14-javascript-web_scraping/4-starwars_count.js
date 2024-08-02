#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];
let movie = 0;
const charactersArray = [];
const targetUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const result = film.results;
    for (let i = 0; i < result.length; i++) {
      charactersArray.push(result[i].characters);
    }
    charactersArray.forEach(array => {
      array.forEach(characterUrl => {
        if (characterUrl === targetUrl) {
          movie++;
        }
      });
    });
  }
  console.log(movie);
});
