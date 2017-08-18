var arr = [24, 8, 23, 3];

function linearSearch(num, arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] === num){
      return console.log(i);
    }
  }
  return console.log('false');
}

linearSearch(8, arr);
linearSearch(-99, arr);
