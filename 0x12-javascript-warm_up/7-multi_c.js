#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!parseInt(args[2])) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < args[2]; i++) {
  console.log('C is fun');
}
