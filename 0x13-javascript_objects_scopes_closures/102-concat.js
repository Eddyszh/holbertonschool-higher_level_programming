#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return;
  }
  fs.appendFileSync(process.argv[4], data, function (err) {
    if (err) {

    }
  });
});

fs.readFile(process.argv[3], 'utf8', function (err, data) {
  if (err) {
    return;
  }
  fs.appendFileSync(process.argv[4], data, function (err) {
    if (err) {

    }
  });
});
