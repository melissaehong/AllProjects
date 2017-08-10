function each(arr, callback) {
  // loop through the array
  for(var i = 0; i < arr.length; i++) {
    callback(arr[i]); // invoking the callback many times... delegation!
  }
}
// call the each function
each([1,2,3], function(num) { alert(num + " I am from the callback!"); })
