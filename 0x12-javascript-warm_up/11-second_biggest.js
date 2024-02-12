#!/usr/bin/node

const process = require('process');
const args = process.argv;

let largest = parseInt(args[2]);
let secondLargest;

if (!args[2]) {
  secondLargest = 0;
} else if (args.length <= 3) {
  secondLargest = 0;
}

for (let i = 2; i < args.length; i++) {
  if (args[i] > largest) {
    secondLargest = largest;
    largest = parseInt(args[i]);
  }
}

console.log(secondLargest);
