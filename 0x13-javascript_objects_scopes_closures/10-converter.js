#!/usr/bin/node
exports.converter = function (base) {
  return function (newBase) {
    return newBase.toString(base);
  };
};
