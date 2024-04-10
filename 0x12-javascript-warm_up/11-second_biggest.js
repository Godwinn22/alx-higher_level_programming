#!/usr/bin/node

// Extract command line arguments starting from index 2
const args = process.argv.slice(2);

// Function to find the second biggest integer in the list of arguments
function findSecondBiggestInteger () {
  // If no arguments passed or only one argument, print 0 and return
  if (args.length === 0 || args.length === 1) {
    console.log(0);
    return;
  }

  // Convert all arguments to integers
  const integersArray = args.map(Number);

  // Sort the integers in descending order
  integersArray.sort((a, b) => b - a);

  // Iterate through the sorted array to find the second biggest integer
  let secondBiggest = integersArray[0];
  for (let i = 1; i < integersArray.length; i++) {
    if (integersArray[i] < secondBiggest) {
      secondBiggest = integersArray[i];
      break; // Found the second biggest integer, exit the loop
    }
  }

  console.log(secondBiggest);
}

// Call the function to find the second biggest integer
findSecondBiggestInteger();
