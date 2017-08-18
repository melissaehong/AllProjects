

array1 = [0, -1, 2, -3, 4, -5, 6]

function removingNegs(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[arr.length-1] < 0){
      arr.pop();
    }
    if (arr[i] < 0){
      temp = arr[i];
      arr[i] = arr[arr.length-1];
      arr[arr.length-1] = temp;
      arr.pop();
    }
  }
  arr.sort();
  console.log(arr);
}

removingNegs(array1);
