
    function removeBlanks(str) {
    var str1 = ' ';
    for (var i = 0; i < str.length; i += 1 ){
      if (str[i] !== ' ' ){
        str1 += str[i];
        }
      }
      return str1;
    }

    function acronyms(str){
    str1 = '',
    initial = true;
    for (var i = 0; i < str.length; i += 1){
      if (str[i] === " "){
        initial = true;
        continue;
      }
      if (initial) {
        initial = false;
        str1 += str[i];
        }
      }
      return str1.toUpperCase();
    }
