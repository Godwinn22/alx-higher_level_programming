#!/usr/bin/node

const firstArg = process.argv[2];
const secArg = process.argv[3];
if (firstArg && secArg) {
  console.log(firstArg + ' is ' + secArg);
} else if (firstArg) {
  console.log(firstArg + ' is ' + secArg);
} else {
  console.log(firstArg + ' is ' + secArg);
}
