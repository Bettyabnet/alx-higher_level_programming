#!/usr/bin/node
/*
 * factorial
 */
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
const result = factorial(num);

console.log(result);
