#!/usr/bin/node

const cuadroBase = require('./4-rectangle');

class Square extends cuadroBase {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let j = 0;
        for (; j < this.width; j++) {
          process.stdout.write('C');
        }
        if (j === this.width) {
          console.log('');
        }
      }
    }
  }
}
module.exports = Square;
