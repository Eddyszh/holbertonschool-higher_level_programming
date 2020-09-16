#!/usr/bin/node
if (process.argv.slice(2).length === 0 || process.argv.slice(2).length === 1) {
  console.log(0);
} else {
  console.log(process.argv.splice(2, process.argv.length - 1).sort().reverse()[1]);
}
