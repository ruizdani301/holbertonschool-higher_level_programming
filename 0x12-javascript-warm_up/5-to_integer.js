#!/usr/bin/env node
let num = parseInt(process.argv[2]);
if (num != NaN)
  console.log("My number is " + num);
else
  console.log("Not a number");
