#!/usr/bin/node

function factorial (numx) {
  if (numx === 0 || isNaN(numx)) {
    return 1;
  }

  return numx * factorial(numx - 1);
}

const numx = parseInt(process.argv[2]);
console.log(factorial(numx));
