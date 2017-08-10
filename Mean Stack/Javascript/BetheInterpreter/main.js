var hello = "interesting";
function example() {
  var hello = "hi!";
  console.log(hello);
}
example();
console.log(hello);

//hoisting test
var hello;
function example(){
  var hello;
  hello = 'hi!';
  console.log(hello);
}
hello = 'interesting';
example();
console.log(hello);

//results:
//'hi!';
//'interesting';

console.log(first_variable);
var first_variable = "Yipee I was first!";
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);

//hoisting test 2
var first_variable;
function firstFunc(){
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);
first_variable = "Yipee I was first!";
console.log(first_variable);

//results
//undefined
//'Yipee I was first!';

var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//hoisting test 3
var food;
function eat(){
  food = "half-chicken";
  console.log(food);
  var food = "gone";
  console.log(food);
}
food = "Chicken";
eat();
console.log(food);

//results:
//half-chicken;
//gone;
//Chicken;

var new_word = "NEW!";
function lastFunc() {
  new_word = "old";
}
console.log(new_word);

var new_word;
function lastFunc(){
  new_word = "old";
}
new_word = "NEW!";
console.log(new_word);

//results:
//NEW!
