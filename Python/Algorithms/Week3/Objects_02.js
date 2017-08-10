function zipArrays(){
  var arr1 = ['abc', 3, 'yo'];
  var arr2 = [42, 'wassup', true];
  var miniArr = [];
  miniArr.push(arr1);
  for (var i = 0; i < arr1.length; i++){
    if (arr1[i] === arr2[i]){
      miniArr.push(arr2[i]);
    }
  }
    return miniArr;
  }
  //return {'abc': 42, 3: 'wassup', 'yo': true}

  function zipArray(arr1, arr2){
    var arr1 = ['abc', 3, 'yo'];
    var arr2 = [42, 'wassup', true];
    var return1 = {};
    for (var i = 0; i < arr1.length; i += 1){
      return1[arr1[i]] = arr2[i];
    }
    return return1;
  }
