// ###Skyline Heights
// From lovely Burbank you have a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending directly away. Array `[-1,7,3]` would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given `[1,-1,7,3]` return `[1,7]`.

function skylineHeights(arr) {
  // Set up empty array to hold viewable buildings
  var viewableBuildings = [],
      // 0 is our minHeight starting point
      minHeight = 0;

  for (var i = 0; i < arr.length; i += 1) {
    // Iterat through the array, only pushing into the viewableBuildings if it's taller that what was last set as the minHeight.
    if (arr[i] > minHeight) {
      viewableBuildings.push(arr[i]);
      minHeight = arr[i];
    }
  }
  return viewableBuildings;
}


// Filter Range
// Alan is good at breaking secret codes. One tool is to eliminate numbers he knows are outside a certain specific range. Given `array` and values `min` and `max`, remove array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

function filterRange(arr, min, max) {
  // Take advantage of the fact that we've already written a removeAt function a few days ago!
  var i = 0;
  while ( i < arr.length) {
    if (arr[i] < min || arr[i] > max) {
      // If the value at location i is smaller than min or bigger than max, remove it! This takes advantage of the fact that arrays are passed by reference.
      removeAt(arr, i);
    } else {
      i += 1;
    }
  }

  return arr;
}


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
