#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log('code: ', response.statusCode);
});
