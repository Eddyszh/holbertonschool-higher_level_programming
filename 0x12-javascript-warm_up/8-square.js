#!/usr/bin/node
const process = require('process');
const myNum = parseInt(process.argv[2]);

if (!myNum) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('x'.repeat(myNum));
  }
}
