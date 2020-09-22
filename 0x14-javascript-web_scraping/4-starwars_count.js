#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

let count = 0;
const id = 'https://swapi-api.hbtn.io/api/people/18/';
request(argv[2], function (err, res, body) {
  const json = JSON.parse(body);
  for (let i = 0; i < json.count; i++) {
    for (let j = 0; j < json.results[i].characters.length; j++) {
      if (json.results[i].characters[j] === id) {
        count++;
      }
    }
  }
  if (err) {
    return;
  }
  console.log(count);
});
