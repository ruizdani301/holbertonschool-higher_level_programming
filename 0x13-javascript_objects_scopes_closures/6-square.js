#!/usr/bin/node

const cuadro_base = require('./5-square');

class Square extends cuadro_base {
  /*charPrint(c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        let j = 0;
          for (; j < this.width; j++) {
            process.stdout.write('X');
            }
          if (j === this.width) {
            console.log('');
          }
        }
    }
    else {
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
  }*/
  charPrint (c) {
    if (c === undefined) {
      this.#private_print('X');
    }
    else {
      this.#private_print('C');
    }
  }


  #private_print(caracter) {
    for (let i = 0; i < this.height; i++) {
        let j = 0;
          for (; j < this.width; j++) {
            process.stdout.write(caracter);
            }
          if (j === this.width) {
            console.log('');
          }
    }
  }

}
module.exports = Square;
