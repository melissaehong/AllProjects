function removeAt(arr, index){
  if (index >= arr.length) {
    return null;
  }
  var value = arr[index];
  for (var i = index; i < arr.length; i+=1){
  arr[i] = arr[i+1];
  }
  arr.length = arr.length-1;
  return value;
}

function swapArrayPairs(arr){
  for (var i=0; i<arr.length-1; i+=2){
    var temp = arr[i];
    arr[i] = arr[i+1];
    arr[i+1] = temp;
    }
    return arr;
  }

//does not work
function swapArrayPairs2(arr){
  for (var i = arr.length; i >= 2; i-=2){
    var temp = arr[i-1];
    arr[i-1] = arr[i-2];
    arr[i-2] = temp;
  }
  return arr;
}

  /*[0,1,2,3]
  i = 4
  temp = arr[i-1] = arr[3] = 3
  arr[3] = arr[4-2] = arr[2] = 2
  arr[2] = 3

  i = 2

  temp = arr[1] = 1
  arr[1] = arr[0] = 0
  arr[0] = 1

  [2,3,0,1]*/
function arrayRemoveDuplicates(arr) {
var newarr = [];
var item = arr[0];
for(var i = 1; i <= arr.length; i++) {
    if(item != arr[i]) {
        newarr.push(item);
        item = arr[i];
    }
}
return newarr;
}
