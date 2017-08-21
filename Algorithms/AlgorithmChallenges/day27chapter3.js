arr = [4,2,1,3,5];

function minToFront(arr){
  // put lowest value to front, and shift other values backwards
  var min = arr[0];
  var idx = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
      idx = i;
    }
  }
  for (var j = idx; j > 0; j--){
    arr[j] = arr[j-1];
  }
  arr[0] = min;
  console.log(arr);
}

//minToFront(arr);


arr1 = [1,2,3,4,5,6]
function reverse(arr){
// reverse values without the use of a second array
for (var i = 0; i < arr.length/2; i++){
 temp = arr[i];
  arr[i] = arr[arr.length-1-i];
  arr[arr.length-1-i] = temp;
}
console.log(arr);
}

//reverse(arr1);

function rotate(arr, shiftBy){
// shift an array to the right by the parameter shiftBy
for (var j = 0; j < shiftBy; j++){
  temp = arr[arr.length-1];
  for (var i = arr.length-1; i > 0 ; i--){
    arr[i] = arr[i-1];
  }
  arr[0] = temp;
}
console.log(arr);
}

//rotate(arr1, 2);

arr = [1,2,3,4,6,5];


function filterRange(arr, max, min){
for (var j = 0; j < arr.length-1; j++){
  for (var i = 0; i <= arr.length-1; i++){
    temp = arr[i];
    if (arr[i] > min && arr[i] < max){
    arr[i] = arr[i+1];
    }
  }
  arr[arr.length-1] = temp;
  arr.pop();
  }
  console.log(arr);
}

filterRange(arr, 6, 1);

function concat(){

}

function skylineHeights(){

}

function removeNegs(){

}

function secondToLast(){

}

function nthToLast(){

}

function secondLargest(){

}

function nthLargest(){

}

function creditCardValid(){

}
