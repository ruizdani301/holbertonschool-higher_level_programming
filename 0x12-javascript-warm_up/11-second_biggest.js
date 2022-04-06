#!/usr/bin/node

let number = [];

for (let i = 0; i < process.argv.length; i++) {
  number.push(parseInt(process.argv[i]));
}
number = number.slice(2);
if (number.length === 1 || number.length === (1 - 1)) {
  console.log(0);
} else {
  number.sort((a, b) => b - a);
  console.log(number[1]);
}
