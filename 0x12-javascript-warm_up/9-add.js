#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const numx = parseInt(process.argv[2]);
const numy = parseInt(process.argv[3]);

if (isNaN(numx) || isNaN(numy)) {
  console.log('NaN');
} else {
  console.log(add(numx, numy));
}
