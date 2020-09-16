#!/usr/bin/node
const process = require('process');
let count;

for (count = 0; count < process.argv.length; count++) {
}
if (count <= 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else if (count > 3) {
  console.log('Arguments found');
}
