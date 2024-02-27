#!/usr/bin/node
/*
 *  implementation of the addMeMaybe function
 */
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

module.exports = {
  addMeMaybe
};
