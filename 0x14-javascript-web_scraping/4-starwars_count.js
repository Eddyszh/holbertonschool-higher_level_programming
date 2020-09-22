#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  let count = 0;
  if (err) {
    return;
  }
  const json = JSON.parse(body);
  for (const film of json.results) {
    for (const character of film.characters) {
      if (character.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
