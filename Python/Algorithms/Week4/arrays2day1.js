function isBalanced(arr) {
  if (!(arr instanceof Array)){
    return false;
  }

  var sum = 0;

  for (var idx = 0; idx < arr.length; idx++){
    sum += arr[idx];
  }

  var halfSum = 0;

  if (sum / 2 == halfSum) { return true;}

  for (var idx = 0; idx < arr.length; idx ++){
    halfSum += arr[idx];
    if (sum / 2 == halfSum) { return true; }
  }
  return false;
}

function balanceIdx(arr) {
  if (!(arr instanceof Array)) {
    return -1;
  }

  var rightSum = 0;

  for (var idx = 0; idx < arr.length; idx ++) {
    rightSum -= arr[idx];
    if (leftSum == rightSum) {
      return idx;
    }

    leftSum += arr[idx];
  }
  return -1;
}
