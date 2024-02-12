#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (!parseInt(args[2])) {
  console.log('Missing size');
}
for (let i = 0; i < args[2]; i++) {
  let line = '';
  for (let j = 0; j < args[2]; j++) {
    line += 'X';
  }
  console.log(line);
}
