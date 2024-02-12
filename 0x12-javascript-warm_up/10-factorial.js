#!/usr/bin/node

const process = require('process');
const args = process.argv;

function factorial (n) {
  if (isNaN(n) || n < 0 || n === 0) { return (1); }
  return (n * factorial(n - 1));
}

console.log(factorial(args[2]));
