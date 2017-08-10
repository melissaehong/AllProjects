function firstDuplicate(a) {
  var findFirstDup = {};
  for (var i of a) {
    if (findFirstDup[i]) return console.log(i);
    findFirstDup[i] = i;
    console.log(findFirstDup);
    console.log(findFirstDup[i])
  }
 return console.log(-1);
}

x = [1,2,3,4,5,34,6,7,67,1];

firstDuplicate(x)

function containsDuplicates(a) {
    var answer = false;
    for(var i=0; i<a.length; i++){
        for (var x = 0; x < i; x++){
            if (a[x] === a[i]){
                answer = true;
            }
        }
    }
    return answer;
}
