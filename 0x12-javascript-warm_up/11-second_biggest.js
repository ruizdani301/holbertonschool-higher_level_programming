#!/usr/bin/node

if (process.argv === 3 || process.argv == 4) {
  console.log(0);
}
let numeros = process.argv.slice(2);
numeros.map(sort(function (a, b) { return b - a; }));
console.log(numero[1])

