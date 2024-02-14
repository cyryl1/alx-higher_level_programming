#!/usr/bin/node
const dict = require('./101-data').dict;

const occByUserId = {};

for (const id in dict) {
  const occurrences = dict[id];

  if (!occByUserId[occurrences]) {
    occByUserId[occurrences] = [];
  }

  occByUserId[occurrences].push(id);
}
console.log(occByUserId);
