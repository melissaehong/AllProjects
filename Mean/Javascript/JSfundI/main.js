var x = [3,5,'Dojo', 'rocks', 'Michael', 'Sensei'];
for (var i = 0; i < x.length; i++){
  console.log(x[i]);
}

x.push(100);
console.log(x);

var x = ['hello', 'world', 'JavaScript is Fun'];
console.log(x);

var sum = 0;
for (var i = 0; i<501; i++){
  sum+=i;
}
console.log(sum);

var array = [1, 5, 90, 25, -3, 0];
var min = array[0];
for (var i = 1; i < array.length; i++){
  if (array[i] < min){
    min = array[i];
  }
}
console.log(min);

var array = [1, 5, 90, 25, -3, 0];
var sum = array[0];
for (var i = 1; i < array.length; i+=1){
  sum+=array[i];
}
console.log(sum/array.length);

var new_ninja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
};
for (var element in new_ninja){
    console.log(element, new_ninja[element]);
}
