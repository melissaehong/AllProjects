function reverseArr(arr){
  for (var i = 0; i < arr.length / 2; i += 1){
    var temp = arr[i];
    arr[i] = arr[arr.length - (i + 1)];
    arr[arr.length - (i + 1)] = temp;
  }
  return arr;
}

//does not work
  function reverseArray(arr){
      for (var x=0; x<arr.length; x++){
        for (var y=arr.length-1; y>0; y--){
          if (arr[x] > arr[y]){
            var temp = arr[x];
            arr[x] = arr[y];
            arr[y] = temp;
          }
          if (arr[y] > arr[x]){
            var temp = arr[y];
            arr[y] = arr[x];
            arr[x] = temp;
          }
        }
      }
      return arr;
    }

    function minToFront(arr){
      var min = 0;
      for (var i=1; i<arr.length; i+=1){
        if (arr[i] < arr[min]){
          min = i;
        }
      }
      mini = arr[min];
      for (var i=min; i>0; i-=1){
        arr[i] = arr[i-1];
      }
      arr[0] = mini;
      return arr;
    }
