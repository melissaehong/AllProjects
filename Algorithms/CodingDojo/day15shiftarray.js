x = [1,5,10,7,-2]

function shiftArray(arr){
  temp = arr[0];
  for (var i = 0; i < arr.length-1; i++){
    arr[i] = arr[i+1];
    console.log(arr);
  }
  arr[arr.length-1] = temp;
  console.log(arr);
}

shiftArray(x);

/*
arr[0] = 5;
arr[1] = 10
arr[2] = 7;
arr[3] = -2;
arr[4] = 0;
*/
