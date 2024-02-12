#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!args[2]) {
  console.log('0');
} else if (args.length <= 3) {
  console.log('0');
}
let largest = parseInt(args[2]);
let secondLargest;
for (let i = 2; i < args.length; i++) {
  if (args[i] > largest) {
    secondLargest = largest;
    largest = parseInt(args[i]);
  }
}

console.log(secondLargest);
