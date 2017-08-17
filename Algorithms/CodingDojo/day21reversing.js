X = [-3, 5, 1, 3, 2, 10];
console.log(X);
function reversing(arr){
  for (var i = 0; i < Math.floor(arr.length/2); i++){
    var temp = arr[i];
    arr[i] = arr[arr.length-1-i];
    arr[arr.length-1-i] = temp;
  }
  console.log(arr);
}

reversing(X);
