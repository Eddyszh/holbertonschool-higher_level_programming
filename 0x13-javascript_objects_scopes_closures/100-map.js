#!/usr/bin/node
const newList = require('./100-data').list;

console.log(newList);
console.log(newList.map((i, n) => i * n));
