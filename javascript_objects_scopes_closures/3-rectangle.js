#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let printf = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        printf = printf + 'x';
      }
      console.log(printf);
    }
  }
}

module.exports = Rectangle;
