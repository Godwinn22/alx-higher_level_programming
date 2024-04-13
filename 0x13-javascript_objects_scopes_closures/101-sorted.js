#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

// Iterate over the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the occurrences key doesn't exist in the sorted dictionary, initialize it with an empty array
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  // Push the user ID to the array corresponding to the occurrences key
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
