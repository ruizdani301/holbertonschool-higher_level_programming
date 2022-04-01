#!/usr/bin/env node
function factorialRecursivo (numx)
{
/* no se si poner el let afuera*/
  let numx = parseInt(process.argv[2]);
  if (numx == NaN || numx == 0)
  {
    return (1);
	}
	console.log(numx * factorialRecursivo (numx-1));
}
