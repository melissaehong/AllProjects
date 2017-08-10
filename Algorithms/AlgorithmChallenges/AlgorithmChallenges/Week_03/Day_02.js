// Zip Arrays into Map
// Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For `arr1 = ["abc", 3, "yo"]` and `arr2 = [42, "wassup", true]`, return `{"abc": 42, 3: "wassup", "yo": true}`.
function zipArrsIntoMap(arr1, arr2){
  var objToReturn = {};

  for (var i = 0; i < arr1.length; i += 1){
    objToReturn[arr1[i]] = arr2[i];
  }
  
  return objToReturn;
}
