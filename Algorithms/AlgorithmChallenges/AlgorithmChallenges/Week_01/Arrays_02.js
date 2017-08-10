// Remove At
// Given array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except `pop()`. Think of `PopFront(arr)` as equivalent to `RemoveAt(arr,0)`.

function removeAt(arr, idx){
  if ( idx >= arr.length ) { return null; }
  // Store value in temporary variable
  var valToReturn = arr[idx];
  // Overwrite array contents from the idx to back of arr
  for (var i = idx; i < arr.length; i += 1) {
    arr[i] = arr[i + 1];
  }
  // Shorten the array by 1
  arr.length = arr.length - 1;
  // Return the value
  return valToReturn;
}



// Swap Array Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change final element. For `[1,2,3,4]`, return `[2,1,4,3]`. For `[false,true,42]`, return `[true,false,42]`.

function swapArrPairs(arr){
  // Iterate through array by 2s, swapping the value with the value at position to the right
  for (var idx = 0; idx < arr.length - 1; idx += 2) {
    var temp = arr[idx];
    arr[idx] = arr[idx + 1];
    arr[idx + 1] = temp;
  }

  return arr;
}

// Array Remove Duplicates
// Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together.

function removeDupes(arr){
  var idx = 0;
  // Iterate through array, asking if the value to the right of where we are is the same
  // Each pass through the loop, either idx will increase by one or arr will shorten in length by 1
  while( idx < arr.length ) {
    if (arr[idx] === arr[idx + 1]) {
      // Take advantage of our removeAt function for this one!
      // This will shorten the array by 1
      removeAt(arr, idx + 1);
    } else {
      // It was a different value, so just move idx forward
      idx += 1;
    }
  }
  return arr;
}
