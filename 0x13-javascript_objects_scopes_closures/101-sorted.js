#!/usr/bin/node
const dict = require('./101-data').dict;
const newDcit = {};
for (const key in dict) {
  if (newDcit[dict[key]] === undefined) {
    newDcit[dict[key]] = [];
  }
  newDcit[dict[key]].push(key);
}
console.log(newDcit);
