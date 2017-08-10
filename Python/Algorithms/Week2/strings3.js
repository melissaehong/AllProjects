function bookIndex(arr){
  var str = '',
  pages = false;
  for (var i = 1; i < arr.length; i += 1){
    if (arr[i] !== arr[i-1]+1){
      pages = false;
      str += arr[i-1] + ', ';
    }
    else {
      if (!pages){
        pages = true;
        str += arr[i-1] + '-';
      }
    }
  }
  str += arr[arr.length-1];
  return str;
}
