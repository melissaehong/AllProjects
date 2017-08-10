var hello = 'interesting';
function example(){
  var hello = 'hi!';
  console.log(hello);
}
example();
console.log(hello);

// var hello;
// function example() {
//    var hello;
//    hello = 'hi!';
//    console.log(hello);
// }
// example();
// console.log(hello);

// hello = 'interesting'
// example();
// hi!
// console.log(hello);
// interesting

console.log(first_variable);
var first_variable = 'Yipee I was first!';
function firstFunc(){
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);

// var first_variable
// function firstFunct(){
//  var first_variable
//  first_variable = "Not anymore!"
//  console.log(first_variable);
// }
// console.log(first_variable);
// first_variable = 'Yipee I was first!';
// console.log(first_variable);

// Undefined
// "Yipee I was first!"

var food = "chicken";
function eat(){
  food = 'half-chicken';
  console.log(food);
  var food = 'gone';
  console.log(food);
}
eat();
console.log(food);

// var food
// function eat(){
//  var food;
//  food = 'half-chicken'
//  console.log(food);
//  food = 'gone'
//  console.log(food)
// }
// food = 'chicken'
// eat();
// console.log(food);

// 'half-chicken'
// 'gone'
// 'chicken'

var new_word = 'NEW!';
function lastFunc(){
  new_word = 'old';
}
console.log(new_word);

// var new_word
// function lastFunc(){
//  var new_word
//  new_word = 'old'
// }
// new_word = "NEW!"
// console.log(new_word);

// 'NEW!'
