#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

let count = 0;
let id = 1;
let dict = {};
request(argv[2], function (err, res, body) {
  if (err) {
    return;
  }
  let json = JSON.parse(body);
  for (let i = 0; i < json.length; i++) {
    if (json[i].userId == id) {
      if (json[i].completed === true) {
        count++;
      }
    } else {
      dict[id] = count;
      count = 0;
      if (json[i].userId == id + 1) {
        if (json[i].completed === true) {
          count++;
        }
      }
      id++;
    }
  }
  console.log(dict);
});
