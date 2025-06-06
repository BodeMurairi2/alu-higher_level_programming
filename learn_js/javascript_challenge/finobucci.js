#!/usr/bin/node

function finobucci (number) {
  const sequence = [];
  let a = 0;
  let b = 1;
  for (let i = 0; i < number; i++) {
    sequence.push(a);
    const temp = a;
    a = b;
    b = temp + b;
  }
  let sum_even_numbers = 0;
  for (const nums of sequence) {
    if (nums < 4000000 && nums % 2 === 0) {
      sum_even_numbers = sum_even_numbers + nums;
    }
  }
  print(`Sums of all sequence number less than 4000000 and even in the finobucci sequence is: ${sum_even_numbers}`);
}

finobucci(25);
