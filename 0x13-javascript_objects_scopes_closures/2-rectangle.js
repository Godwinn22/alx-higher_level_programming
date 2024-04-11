#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(h) || !Number.isInteger(w)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
