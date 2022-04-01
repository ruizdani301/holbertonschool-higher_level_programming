#!/usr/bin/env node

let numx = parseInt(process.argv[2]);
let numy = parseInt(process.argv[3]);

function add(a, b)
{
  return (a + b);
}
  let pro = (process.argv).lenght;
  if (numx == NaN || numy == NaN ||  pro < 3)
    console.log("Missing size");
  else
    console.log(add(numx, numy));
