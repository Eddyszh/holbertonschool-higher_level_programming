#!/usr/bin/node
const process = require('process');
const myNum = parseInt(process.argv[2]);

if (!myNum) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
