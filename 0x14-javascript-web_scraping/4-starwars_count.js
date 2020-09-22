#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const id = 'https://swapi-api.hbtn.io/api/people/18/';
request(argv[2], function (err, res, body) {
  let count = 0;
  if (err) {
    return;
  }
  const json = JSON.parse(body);
  for (const film of json.results) {
    for (const character of film.characters) {
      if (character === id) {
        count++;
      }
    }
  }
  console.log(count);
});
