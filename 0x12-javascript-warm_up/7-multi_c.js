#!/usr/bin/node

let x = process.argv[2];
if (x) {
  for (x; x > 0; x--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
