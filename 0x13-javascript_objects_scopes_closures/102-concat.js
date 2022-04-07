#!/usr/bin/node

const fs = require('fs');

const dataOne = fs.readFileSync(process.argv[2], 'utf8');

const dataTwo = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFile(process.argv[4], dataOne + dataTwo, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
