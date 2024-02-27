#!/usr/bin/node
/*
 * module that defines a Square class inheriting from the Rectangle class
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
