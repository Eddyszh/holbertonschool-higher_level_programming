#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) {
    return;
  }
  const dict = {};
  const json = JSON.parse(body);
  for (const task of json) {
    if (task.completed === true) {
      if (task.userId in dict) {
        dict[task.userId] += 1;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
});
