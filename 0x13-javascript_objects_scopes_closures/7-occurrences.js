#!/usr/bin/node
/*
 *  module that exports a function to return the number
 *  of occurrences of a search element in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
