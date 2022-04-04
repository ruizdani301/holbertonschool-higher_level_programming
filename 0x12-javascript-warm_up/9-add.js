#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const numx = parseInt(process.argv[2]);
const numy = parseInt(process.argv[3]);

const pro = (process.argv).lenght;
if (isNaN(numx) || isNaN(numy) || pro < 3) {
  console.log('Missing size');
} else {
  console.log(add(numx, numy));
}
