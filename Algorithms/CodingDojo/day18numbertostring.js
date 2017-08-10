x = [-1, -3, 2]

function numberToString(arr){
  for (var i = 0; i < arr.length; i++){
    if(arr[i] < 0){
      arr[i] = 'Dojo';
    }
  }
  console.log(arr);
}

numberToString(x)
