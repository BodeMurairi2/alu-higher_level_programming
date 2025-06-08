#!/usr/bin/node

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let printf = '';
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        printf = printf + 'X';
      }
      console.log(printf);
      prints = '';
    }
  }
};

module.exports = Rectangle;
