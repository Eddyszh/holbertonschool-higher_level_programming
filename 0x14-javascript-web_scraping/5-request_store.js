#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const fs = require('fs');

request(argv[2], function (err, res, body) {
  if (err) {
    return;
  }
  fs.writeFile(argv[3], res.body, function (err) {
    if (err) {
    }
  });
});
