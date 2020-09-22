#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (err, res, body) {
  if (err) {
    return;
  }
  const json = JSON.parse(body);
  for (const character of json.characters) {
    request(character, function (err, res, body) {
      if (err) {
        return;
      }
      const names = JSON.parse(body);
      console.log(names.name);
    });
  }
});
