#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (err, res, body) {
  const json = JSON.parse(body);
  if (err) {
    return;
  }
  console.log(json.title);
});
