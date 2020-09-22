#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) {
    return;
  }
  console.log('code: ' + res.statusCode);
});
