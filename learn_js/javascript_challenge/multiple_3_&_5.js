#!/usr/bin/node

/* This script calculates the sum of all multiples of 3 and 5 */
function sumMultipleOf3And5 () {
  let sum = 0;
  for (let i = 0; i < 1000; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sum += i;
    }
  }
  console.log(`The sum of all numbers multiple of 3 or 5 is ${sum}`);
}

sumMultipleOf3And5();
