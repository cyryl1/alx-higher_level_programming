#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const args = process.argv;
const url = args[2];
const file = args[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
