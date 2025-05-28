#!/usr/bin/node

const a = parseInt(process.argv.slice(2)[0]);
const b = parseInt(process.argv.slice(2)[1]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
