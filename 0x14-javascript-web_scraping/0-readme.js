#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const file = args[2];

if (!file) {
  console.error('Usage: ./script.js <filename>');
  process.exit(1);
}

fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(data);
  }
});
