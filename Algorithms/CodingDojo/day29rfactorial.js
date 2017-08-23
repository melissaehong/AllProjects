function rFactorial(num){
  if (num === 1){
    return 1;
  }
  else{
  return rFactorial(num-1) * num;
  }
}

//console.log(rFactorial(4));

function iFibonacci(num){
  var fibs = [0,1];
  for (var i = 0; i < num; i++){
    fibs.push(fibs[0] + fibs[1]);
    fibs.shift();
  }
  return fibs[0];
}

//console.log(iFibonacci(3));

function rFibonacci(num){
  if (num === 0){
    return 0;
  }
  if (num === 1){
    return 1;
  }
  else{
    return rFibonacci(num-2) + rFibonacci(num-1);
  }
}

//console.log(rFibonacci(6));


var arr = [-90,-19,0,2,12,29,33,190,320];

function findMidPoint(min, max){
  midpoint = (max +(min+1)/2);
  return Math.floor(midpoint);
  }

function rBS(arr, search, min, max){
  if (max < min){
    return false;
  }
  else {
    midpoint = findMidPoint(min, max);
    if (arr[midpoint] > search){
      return rBS(arr, search, min, midpoint-1);
    }
    if (arr[midpoint] < search){
      return rBS(arr, search, midpoint+1, max);
    }
    else {
      return arr.indexOf(search);
    }
  }
}

function iBS(arr, search, min, max){
  if (max < min){
    return false;
  }
  else {
    for (var i = 0; i < arr.length; i++){
      midpoint = findMidPoint(min, max);
      if (arr[midpoint] > search){
        max = midpoint-1;
      }
      if (arr[midpoint] < search){
        min = midpoint+1;
      }
      else {
        return arr.indexOf(search);
      }
    }
  }
}

//console.log(iBS(arr, 12, 0, 9));

arr = [4,3,1,6,7,2];

function bubbleSort(arr){
  var count = 0;
    var unsorted;
    do {
      unsorted = false;
      for (var i = 0; i < arr.length- 1 - count; i++){
        if (arr[i] > arr[i+1]){
          swap (arr, i, i+1);
          unsorted = true;
        }
      }
      count++;
    }
    while(unsorted === true);
 console.log(arr);
}

function swap(arr, indexOne, indexTwo){
  var temp = arr[indexOne];
  arr[indexOne] = arr[indexTwo];
  arr[indexTwo] = temp;
}

bubbleSort(arr);
