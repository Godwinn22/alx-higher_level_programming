#!/usr/bin/node

exports.esrever = function (list) {
  let start = 0;
  // to get the end element
  let end = list.length - 1;

  while (start < end) {
    // we store the original value of the first element.
    const temp = list[start];
    // we swap the first with the last, and just keep iterating.
    list[start] = list[end];
    // then swap our temporary variable back into its place.
    list[end] = temp;
    // now that we've swapped them, we can increment / decrement appropriately.
    start++; // move towards the middle
    end--; // move away from the middle
  }
  return list;
};
