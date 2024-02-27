#!/usr/bin/node
/*
 * module that defines a Rectangle class with a c
 * onstructor that takes w and h
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
