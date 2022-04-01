#!/usr/bin/env node
let num = parseInt(process.argv[2]);
if (num != NaN && num >= 0)
{
  for(let i = 0; i < num; i++)
  {
    for(let j = 0; j < num; j++)
      process.stdout.write("x");
  }
  console.log("")
}
else
  console.log("Missing size");
