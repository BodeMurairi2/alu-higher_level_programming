#!/usr/bin/node

const x = process.argv.slice(2);

if (parseInt(x[0])) {
  for (let i = 0; i < parseInt(x[0]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
