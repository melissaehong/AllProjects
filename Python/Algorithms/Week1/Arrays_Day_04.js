function skylineHeights(){
  var arr = [1,-1,7,3];
  var newarr = [],
  min = 0;
  for (var i = 0; i < arr.length; i += 1){
    if (arr[i] > min){
      newarr.push(arr[i]);
      min = arr[i];
    }
  }
  return newarr;
  }

  function skylineHeights1(){
    var arr = [1,-1,7,3];
    var newarr = [],
    min = 0;
    for (var i = 0; i < arr.length; i += 1){
      if (arr[i] < min){
        arr.splice(i, 1);
        min = arr[i];
      }
      if (arr[i] < 0){
        arr.splice(i, 1);
      }
    }
    return arr;
    }

function filterRange(arr, min, max){
  arr = [0,1,2,3,4];
  max = 3;
  min = 1;
  for (var i = 0; i < arr.length; i += 1){
    if (arr[i] > max){
      arr.splice(i, 1);
    }
    if (arr[i] < min){
      arr.splice(i, 1);
    }
  }
  return arr;
}
