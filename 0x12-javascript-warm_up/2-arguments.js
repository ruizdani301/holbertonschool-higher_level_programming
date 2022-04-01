#!/usr/bin/env node
let args = process.argv;
if (args.length >= 3)
  console.log("Arguments found");
else if (args.length === 3)
  console.log("Argument found");
else
  console.log("No argument");
