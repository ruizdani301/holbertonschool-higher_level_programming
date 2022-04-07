#!/usr/bin/node

const fs = require('fs');

const dataOne = fs.readFileSync(process.argv[2],

  { encoding: 'utf8' });

const dataTwo = fs.readFileSync(process.argv[3],

  { encoding: 'utf8' });

fs.writeFile(process.argv[4], dataOne + dataTwo, function (error) {
  if (error) {
    console.log(error);
  } else {
    console.log('El archivo fue creado');
  }
});
