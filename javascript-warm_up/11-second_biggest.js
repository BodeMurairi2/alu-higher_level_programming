#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
  process.exit(1);
}

let first = -Infinity;
let second = -Infinity;

for (const arg of args) {
  if (arg > first) {
    second = first;
    first = arg;
  } else if (arg > second && arg !== first) {
    second = arg;
  }
}
if (second === -Infinity) {
  console.log(0);
} else {
  console.log(second);
}
