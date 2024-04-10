#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const a = parseInt(arg1);
const b = parseInt(arg2);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('Nan');
  } else {
    console.log(a + b);
  }
}
add(a, b);
