arr = [4,5,1,7,2];

function selectionSort(arr){
  var min;
  for (var i = 0; i < arr.length-1; i++){
    min = i;
    for (var j = i+1; j < arr.length; j++){
      if (arr[j] < arr[min]){
        min = j;
      }
    }
    if (min !== i){
      swap(arr, i, min);
    }
  }
  console.log(arr);
}

function swap(arr, indexOne, indexTwo){
  temp = arr[indexOne];
  arr[indexOne] = arr[indexTwo];
  arr[indexTwo] = temp;
}

//selectionSort(arr);

function insertionSort(arr){
  var element;
  for (var i = 1; i < arr.length-1; i++){
    element = arr[i];
    j = i;
    while (j > 0 && arr[j-1] > element){
      arr[j] = arr[j-1];
      j = j-1;
    }
    arr[j] = element;
  }
}

//insertionSort(arr);

var a = [34, 203, 3, 746, 200, 984, 198, 764, 9];

function mergeSort(arr)
{
    if (arr.length < 2)
        return arr;

    var middle = parseInt(arr.length / 2);
    var left   = arr.slice(0, middle);
    var right  = arr.slice(middle, arr.length);

    return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right)
{
    var result = [];

    while (left.length && right.length) {
        if (left[0] <= right[0]) {
            result.push(left.shift());
        } else {
            result.push(right.shift());
        }
    }

    while (left.length)
        result.push(left.shift());

    while (right.length)
        result.push(right.shift());

    return result;
}

//console.log(mergeSort(a));

function quickSort(arr, left, right){
   var len = arr.length,
   pivot,
   partitionIndex;


  if(left < right){
    pivot = right;
    partitionIndex = partition(arr, pivot, left, right);

   //sort left and right
   quickSort(arr, left, partitionIndex - 1);
   quickSort(arr, partitionIndex + 1, right);
  }
  return arr;
}

function partition(arr, pivot, left, right){
   var pivotValue = arr[pivot],
       partitionIndex = left;

   for(var i = left; i < right; i++){
    if(arr[i] < pivotValue){
      swap(arr, i, partitionIndex);
      partitionIndex++;
    }
  }
  swap(arr, right, partitionIndex);
  return partitionIndex;
}

function swap(arr, i, j){
   var temp = arr[i];
   arr[i] = arr[j];
   arr[j] = temp;
}


console.log(quickSort(arr, 0, 4));
