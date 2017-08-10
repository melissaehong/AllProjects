function palindrome(str){
  str1 = '';
  for (var i = 0; i <= str.length/2; i++){
    if (str[i] !== str[str.length-1-i]){
    return false;
  }
}
  return true;
}

function palindrome1(str) {
  var expression = /[.,\/#!$%\^&\*;:{}=\-_`~()\?\s]/,
      rightEdge = str.length - 1,
      leftEdge = 0,
      validchar = false;

  while (rightEdge >= leftEdge) {
    if (expression.test(str[rightEdge])) {
      rightEdge -= 1;
      continue;
    }

    if (expression.test(str[leftEdge]) ) {
      leftEdge += 1;
      continue;
    }
    validchar = true;
    if (str[rightEdge].toUpperCase() !== str[leftEdge].toUpperCase() ) {
      return false;
    }
    leftEdge += 1;
    rightEdge -= 1;
  }
  return validchar;
}
