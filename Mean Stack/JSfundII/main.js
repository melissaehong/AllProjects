function firstFunc(){
var x = [3,5,'Dojo', 'rocks', 'Michael', 'Sensei'];
for (var i = 0; i < x.length; i++){
  console.log(x[i]);
}
x.push(100);
console.log(x);
}

function secondFunc(){
var x = ['hello', 'world', 'JavaScript is Fun'];
console.log(x);
}

function sum(){
var sum = 0;
for (var i = 0; i<501; i++){
  sum+=i;
}
console.log(sum);
}

function ninja(){
  var new_ninja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}
for (var element in new_ninja){
    console.log(element, new_ninja[element]);
}
}


var a = grandSum(1,10);
function grandSum(x,y){
  var sum = 0;
  for (var i = x; i < y; i++){
    sum+=i;
  }
  console.log(sum);
}

var b = min();
function min(){
var array = [1, 5, 90, 25, -3, 0];
var min = array[0];
for (var i = 1; i < array.length; i++){
  if (array[i] < min){
    min = array[i];
  }
}
console.log(min);
}

var c = avg();
function avg(){
var array = [1, 5, 90, 25, -3, 0];
var sum = array[0];
for (var i = 1; i < array.length; i+=1){
  sum+=array[i];
}
console.log(sum/array.length);
}
