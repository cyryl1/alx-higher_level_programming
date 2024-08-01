#!/usr/bin/node

const request = require('request');

const args = process.argv;
const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.log(`Failed to fetch movie with ID: ${id}`);
  }
});
