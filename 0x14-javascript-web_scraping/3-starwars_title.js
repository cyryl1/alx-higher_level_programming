#!/usr/bin/node

const request = require('request');

const args = process.argv;
const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, body) => {
  if (error) {
    console.log(error);
  }

  try {
    const film = JSON.parse(body);
	  console.log(film);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
