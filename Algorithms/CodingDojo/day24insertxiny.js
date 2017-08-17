array = [1,3,5,7]
X = 10;
Y = 2;

function insertXInY(arr, x, y){
  arr.push(0);
  for (var i = arr.length-1; i > y; i--){
      arr[i] = arr[i-1];
  }
  arr[y] = x;
  console.log(arr);
}

insertXInY(array, X, Y);
