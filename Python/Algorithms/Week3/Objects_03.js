function repeated(str){
  var str = 'abcaaaabcc';
  var count = 0;
  for (var i = 0; i < str.length; i++){
      if (str[i] === str[i+1]){
      count++;
      console.log(str[i]);
      console.log(count);
      }
    }
  return str;
}
