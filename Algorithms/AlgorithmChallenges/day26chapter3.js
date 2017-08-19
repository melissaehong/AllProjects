arr = [1,2,3,4]

function pushFront(arr, val){
  // given array and additional value, insert this value at the begiinning of the array
  // do not use any built-in array methods
  arr.push(0);
  for (var i = arr.length-1; i > 0; i--){
    arr[i] = arr[i-1];
    console.log(arr);
  }
  arr[0] = val;
  console.log(arr);
}

//pushFront(arr, 0)

function insertAt(arr, idx, val){
  //given array, index, and additional value, insert the value into array at given index
  // no built in arrays
  arr.push(0);
  //[1,2,3,4,0]
  for (var i = arr.length-1; i > idx; i--){
    // idx = 1; i > 1;
    // i = 4
    arr[i] = arr[i-1];
    //[1,2,3,4,4]; i = 3;
    //[1,2,3,3,4]; i = 2;
    //[1,2,2,3,4]; i = 1;
  }
  arr[idx] = val;
  // arr[1] = val
  // arr[1] = 11
  console.log(arr);
  //[1,11,2,3,4];
}

//insertAt(arr, 1, 11);

function popFront(arr){
  // given array, remove and return the value at the beginning of the array
  // only can use pop()
  // arr = [1,2,3,4]
  temp = arr[0]
  //temp = 1
  for (var i = 0; i < arr.length-1; i++){
    //i < 3
    arr[i] = arr[i+1];
    // i = 0; arr = [2,2,3,4];
    // i = 1; arr = [2,3,3,4];
    // i = 2; arr = [2,3,4,4];
    // i = 3; break; 3 < 3? NO
    console.log(arr);
  }
  arr[arr.length-1] = temp;
  //[2,3,4,1]
  arr.pop();
  // [2,3,4]
  console.log(temp);
  // 1
  console.log(arr);
  //[2,3,4]
}

//popFront(arr);

function removeAt(arr, idx){
  // given array and an index into array, remove and return the array value at that index
  // only can use pop()
  // arr = [1,2,3,4]
  // idx = 1;
  temp = arr[idx];
  //temp = 1;
  for (var i = idx; i < arr.length-1; i++){
    arr[i] = arr[i+1];
    // i = 1;
    //arr[1] = arr[2];
    //[1,3,3,4];
    // i = 2
    //arr[2] = arr[3];
    //[1,3,4,4];
    // i = 3;
    // 3 < 3? NO
  }
  arr[arr.length-1] = temp;
  //arr[3] = 3
  //[1,2,4,3]
  arr.pop();
  //[1,2,4]
  // 3
  //[1,2,4]
  return (temp, arr);
}

//removeAt(arr, 0);
//console.log(arr);
//console.log(temp);
//removeAt(arr, 1);

//removeAt(arr, 2);

function swapPairs(arr){
//  swap position of successive pairs of values of given array
// if length is odd, do not change the final element
// ex: for [1,2,3,4] return [2,1,4,3]
// ex: for ['Brendan, true, 42'] return [ true, 'Brendan', 42]
// no built in arrays
length = arr.length;
  if (length % 2 === 1){
    length = arr.length-1;
  }
  for (var i = 0; i < length-1; i+=2){
    temp = arr[i];
    arr[i] = arr[i+1];
    arr[i+1] = temp;
  }
  console.log(arr);
}

//swapPairs(arr);
//swapPairs(['Brendan', true, 42]);
//swapPairs([1,2,3,4,5,6,7])

arr = [1,1,2,3,4,4,4,5,5,6]
function removeDuplicates(arr){
//  given a sorted array, remove duplicate values
//  array will already be in order, all duplicate values will be grouped together
// arr = [1,2,3,4,5,6];
// dups = [1,4,4,5]
dups = [];
for (var i = 0; i < arr.length; i++){
  if (arr[i] === arr[i+1]){
    dups.push(arr[i]);
    removeAt(arr, i);
    i -= i;
    // [5]
    //[1,1,2,3,4,4,4,5,5,6,0]
  }
}
return (arr, dups);
}
//removeDuplicates(arr);
//console.log(arr, dups);
