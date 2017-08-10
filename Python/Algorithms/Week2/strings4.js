function parensValid(str){
  var num = 0;
  for (var i = 0; i < str.length; i++){
    if (str[i] == '('){
      num++;
    }
    if (str[i] == ')'){
      num--;
    }
    if ((num) < 0){
      return false;
    }
  }
  return (num === 0);
}
