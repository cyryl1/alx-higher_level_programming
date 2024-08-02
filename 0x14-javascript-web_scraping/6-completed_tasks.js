#!/usr/bin/node

const request = require('request');

const args = process.argv;
const url = args[2];
const result = {};
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    for (let j = 1; j < 11; j++) {
      for (let i = 0; i < todos.length; i++) {
        if (todos[i].userId === j && todos[i].completed) {
          count++;
        }
      }
      result[`${j}`] = count;
      count = 0;
    }
    console.log(result);
  }
});
