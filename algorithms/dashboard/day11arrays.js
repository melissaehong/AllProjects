function createOddArray(Y){
  Y = new Array();
  for (var i = 1; i <= 255; i+=2){
    Y.push(i);
  }
  console.log(Y);
}

//createOddArray('A')

arr1 = [1,3,5,7]

function greaterThanY(arr, y){
  var count = 0;
  for (var i = 0; i < arr.length; i ++){
    if (arr[i] > y){
      count ++
    }
  }
  console.log(count);
}

//greaterThanY(arr1, 3)

function squareValues(arr){
  for (var i = 0; i < arr.length; i++){
    arr[i] = arr[i]*arr[i];
  }
  console.log(arr);
}

//squareValues(arr1)

arr2 = [1,5, 10, -2]

function eliminateNegs(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < 0){
      arr[i] = 0;
    }
  }
  console.log(arr);
}

//eliminateNegs(arr2)

arr3 = [1, 5, 10, -2]

function maxMinAvg(arr){
  sum = 0;
  min = arr[0];
  max = arr[0];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
    if (arr[i] > max){
      max = arr[i];
    }
    sum += arr[i];
  }
  avg = sum/arr.length;
  console.log(max, min, avg);
}

maxMinAvg(arr3)
