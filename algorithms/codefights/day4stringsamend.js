function amendTheSentence(a){
  returnStr = '';
  for (var i = 0; i <a.length; i++){
        if (i === 0 && a.charAt(i) === a.charAt(i).toUpperCase())
      {
      returnStr += a.charAt(i).toLowerCase();
    }
    if(i === 0 && a.charAt(i) === a.charAt(i).toLowerCase()){
      returnStr += a.charAt(i);
    }
  }
  for (var i = 1; i < a.length; i++){
    if(i >0 && a.charAt(i) === a.charAt(i).toUpperCase()){
      returnStr += ' ' + a.charAt(i).toLowerCase();
    }
    else{
          returnStr += a.charAt(i);
    }
  }
  return returnStr;
}

console.log(amendTheSentence('HappyGilmore'))
