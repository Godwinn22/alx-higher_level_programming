#!/usr/bin/node

const arg1 = process.argv[2];
const n = parseInt(arg1);

// Function to compute factorial recursively
function computeFactorial (n) {
  // Base case: if n is NaN or less than 0, return 1
  if (isNaN(n) || n < 0) {
    return 1;
  }
  // Base case: if n is 0 or 1, return 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: return n multiplied by factorial of (n-1)
  return n * computeFactorial(n - 1);
}
console.log(computeFactorial(n));
