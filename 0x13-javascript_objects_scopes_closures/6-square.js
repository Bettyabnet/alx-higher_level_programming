#!/usr/bin/node
/*
 * a class Square that defines a square and 
 * inherits from Square of 5-square.js
 */
const Square = require('./5-square');

class Square1 extends Square {
  charPrint (c) {
    if (!c) this.print();
    else {
      for (let i = 0; i < this.width; i++) console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square1;
