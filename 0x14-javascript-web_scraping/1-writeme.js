#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const file = args[2];
const content = args[3];

if (!file || !content) {
  console.log('Usage: ./script.js <filename> <content>');
  process.exit(1);
}

fs.writeFile(file, content, 'utf-8', (error) => {
  if (error) {
    console.error('error: ', error);
  }
});
