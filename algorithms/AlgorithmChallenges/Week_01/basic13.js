// Print 1-255
// Print all the integers from 1 to 255.

function print1to255() {
  var num = 1;
  // Using a while loop; can also use for loop
  while (num <= 255) {
    console.log(num);
    num = num + 1;
  }
}

// Print Odds 1-255
// Print all odd integers from 1 to 255.

function printOdds1to255() {
  var num = 1;
  // Using a while loop; can also use for loop
  while (num <= 255) {
    console.log(num);
    num = num + 2;
  }
}

// Print Sum 0-255
// Print integers from 0 to 255, and the sum so far.

function printSum1to255() {
  var sum = 0;
  for (var num = 0; num <= 255; num+=1) {
    sum += num;
    console.log("New number:", num, "Sum:", sum);
  }
}

// Iterate Array
// Print all values in a given array.

function printArrayValues(arr) {
  for (var index = 0;index < arr.length;index++) {
    console.log("array[", index, "] is equal to", arr[index]);
  }
}

// Find Max
// Print the largest element in a given array.

function printArrayMax(arr) {
  if (arr.length == 0) {
    console.log("Empty array, no max value.");
    return;
  }
  var max = arr[0];
  for (var idx = 1; idx < arr.length; idx += 1) {
    if (arr[idx] > max) {
      max = arr[idx];
    }
  }
  console.log("Max value is:", max);
}

// Get Average
// Analyze an array's values and print the average.

function printArrayAverage(arr) {
  if (arr.length == 0) {
    console.log("Null arr, no average val");
    return;
  }
  var sum = arr[0];
  for (var idx = 1; idx < arr.length; idx += 1) {
    sum += arr[idx];
  }
  console.log("Average value is:", sum / arr.length);
}

// Array with Odds
// Create an array with odd integers from 1-255.

function oddArray1to255() {
  var oddArray = [];
  for (var num = 1; num <= 255; num += 2) {
    oddArray.push(num);
  }
  return oddArray;
}

// Square the Values
// Given an array, square each value in the array.

function squareArrVals(arr) {
  for (var idx = 0; idx < arr.length; idx += 1) {
    arr[idx] = arr[idx] * arr[idx];
  }
  return arr;
}

// Greater than Y
// Given an array and a value `Y`, count and print the number of array values greater than `Y`.

function numGreaterThanY(arr, y) {
  var numGreater = 0;
  for (var idx = 0; idx < arr.length; idx++) {
    if (arr[idx] > y) {
      numGreater++;
    }
  }
  console.log("%d values greater than %d", numGreater, y);
}

// Zero Out Negative Numbers
// Set negative array values to zero.

function setNegsToZero(arr) {
  for (var idx = 0; idx < arr.length; idx += 1) {
    if (arr[idx] < 0) {
      arr[idx] = 0;
    }
  }
  return arr;
}

// Max, Min, Average
// Given an array, print max, min and average values.

function maxMinAverage(arr) {
  if (arr.length == 0) {
    console.log("Null arr, no min/max/avg");
    return;
  }
  var min = arr[0];
  var max = arr[0];
  var sum = arr[0];
  for (var idx = 1; idx < arr.length; idx+=1) {
    if (arr[idx] < min) { min = arr[idx]; }
    if (arr[idx] > max) { max = arr[idx]; }
    sum += arr[idx];
  }
  console.log("Max value:", max);
  console.log("Min value:", min);
  console.log("Avg value:", sum / arr.length);
}

// Shift Array Values
// Given an array, shift all values forward, dropping the first value and leaving an extra '0' value at the end.

function arrShift(arr) {
  for (var idx = 1; idx < arr.length; idx+=1) {
    arr[idx - 1] = arr[idx];
  }
  arr[arr.length - 1] = 0;
  return arr;
}

// Swap String For Array Negative Values
// Given an array of numbers, replace any negative values with the string 'Dojo'.

function swapStringForNegatives(arr) {
  console.log('hello')
  for (var index = 0; index < arr.length; index += 1) {
    if (arr[index] < 0) { arr[index] = 'Dojo'; }
  }
  return arr;
}
