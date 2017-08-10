function countDown(number){
  count = 0;
  for (var i = number; i >= 0; i --){
    console.log('Counting Down! ' + i);
    count ++;
  }
  console.log('Length: ' + count);
}

// countDown(10)

function printReturn(number1, number2){
  console.log(number1);
  return number2;
}

//printReturn(2,0)

function firstPlusLength(array){
  sum = 0;
  for (var i = 0; i < array.length; i ++){
      if (typeof array[0] === 'number'){
        sum += array[0] + array.length;
      }
      else{
        sum = 'Is not a number!'
      }
  }
  console.log(sum);
}

//me = [0,1,2]
//firstPlusLength(me)

//me2 = 'hi'
//firstPlusLength(me2)

array2 = [1,3,5,7,9,13]
function valuesGreaterThanSecond(array){
  var count = 0;
  for (var i = 0; i < array.length; i++)
    if (array[i] > array[1]){
      console.log("Number " + array[i]);
      count++
    }
    console.log("Values:" + count);
}

//valuesGreaterThanSecond(array2)
array3 = [1]
array4 = [1,3,5,7,9,13]

function valuesGreaterThanSecond2(array){
  var count = 0;
  for (var i = 0; i < array.length; i++)
    if (array[i] > array[1]){
      console.log("Number " + array[i]);
      count++
    }
    if (array.length === 1){
      count = "Array not long enough!"
    }
    console.log("Values: " + count);
}

//valuesGreaterThanSecond2(array3)

function thisLengthThatValue(number1, number2){
  arr = [];
  arr.length = number1;
  if (number1 === number2){
    console.log('Jinx!')
    return;
  }
  for (var i = 0; i < arr.length; i++){
      arr[i] = number2;
  }
  console.log(arr);
}

//thisLengthThatValue(3,3)
//thisLengthThatValue(2,1)

arr3 = [4, 5, 10, -2]

function fitFirstValue(arr){
  b = arr[0];
  c = arr.length;
  var value = '';

  if ( b > c ){
    value += "too big!"
  }
  if( b < c ){
    value += "too small!"
  }
  if( b === c ){
    value += "just right!"
  }
console.log(value)
}

//fitFirstValue(arr3)


function fahrenheitToCelsius(fDegrees){
  celsius = (5/9)*(fDegrees-32)
  console.log(celsius);
}

//fahrenheitToCelsius(45)

function celsiusToFahrenheit(cDegrees){
  fahrenheit = (9/5)*(cDegrees) + 34
  console.log(fahrenheit);
}

//celsiusToFahrenheit(0)

function biggieSize(a){
  for (var i = 0; i < a.length; i++){
    if (a[i] > 0){
      a[i] = 'big';
    }
  }
  console.log(a);
}

//biggieSize(arr3)

function printLowReturnHigh(a){
  var min = a[0];
  var max = a[0]
  for (var i = 0; i < a.length; i++){
    if (a[i] < min){
      min = a[i];
    }
    if (a[i] > max){
      max = a[i];
    }
  }
  console.log(min);
  return max;
}

function printOneReturnAnother(a){
  for (var i = 0; i < a.length; i++){
    console.log(a[a.length-2]);
    if (a[i]%2 === 0){
      return a[i];
    }
  }
}

//printOneReturnAnother(arr3);

function doubleVision(a){
  b = [];
  for (var i = 0; i < a.length; i++){
    c = a[i]*2;
    b.push(c);
  }
  console.log(b);
  console.log(a);
}

//doubleVision(arr3)

//console.log(arr3);
function countPositives(a){
  var count = 0;
  for (var i = 0; i < a.length; i++){
    if (a[i] > 0){
      console.log(a[i])
      count++;
    }
  }
  a[a.length-1] = count;
  console.log(a);
}

//countPositives(arr3)

arr1 = [0,2,4,9,11,13,2,4,6,5,7,9]

function evensAndOdds(arr){
  for (var i = 0; i < arr.length-1; i++){
    if (arr[i]%2 ===1 && arr[i+1]%2 === 1 && arr[i+2]%2 === 1){
      console.log("That's odd!")
    }

    if(arr[i]%2 === 0 && arr[i+1]%2 === 0 && arr[i+2]%2 === 0){
      console.log("Even more so!")
    }
  }
  console.log(arr);
}

//evensAndOdds(arr1)

//console.log(arr1)
function incrementTheSeconds(arr){
  for (var i = 0; i < arr.length; i++){
    if (i%2 === 1){
      arr[i] += 1;
    }
    console.log(arr[i]);
  }
  console.log(arr);
}

//incrementTheSeconds(arr1)

string = ['apple', 'banana', 'cat', 'dog', 'elephant']
function previousLengths(arr){
  for (var i = 0; i < arr.length; i ++)
    arr[0] = arr[arr.length-1].length;
  for (var i = 1; i < arr.length; i++){
    arr[i] = (arr[i].length-1);
  }
  console.log(arr);
}

//previousLengths(string);


arr1 = [0,2,4,9,11,13,2,4,6,5,7,9]
function addSevenToMost(arr){
  b = [];
  for (var i = 1; i < arr.length; i++){
      b.push(arr[i]+7);
  }
  console.log(b);
}

//addSevenToMost(arr1);

var arr2 = [3,1,6,4,2];

function reverseArray(arr){
  b = [];
  for (var i = arr.length-1; i >= 0; i--){
    b.push(arr[i]);
  }
  console.log(b);
}

//reverseArray(arr2);
arr = [1,-3,5];

function outlookNegative(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > 0){
      arr[i] = arr[i]*(-1);
    }
  }
  console.log(arr);
}

//outlookNegative(arr)

arr = ['food', 1, 3, 'food']
arr1 = [2,3,1,3]

function alwaysHungry(arr){
  var count = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] === 'food'){
      console.log('yummy');
    }
    if (arr[i] != 'food'){
      count++;
    }
  }
  if (count === arr.length){
    console.log("I'm hungry!");
  }

}

//alwaysHungry(arr1);

arr1 = [1,2,3,4,5,6];

function swapTowardTheCenter(x){
for (var i = 0; i < 6; i+=3){
  var temp = x[i];
  x[i] = x[x.length - 1 - i];
  x[x.length - 1 - i ] = temp;
}
console.log(x);
}

//swapTowardTheCenter(arr1);

function swapNumb(a, b){
  console.log('before swap: ','a: ', a, 'b: ', b);
  b = b -a;
  a = a+ b;
  b = a-b;
  console.log('after swap: ','a: ', a, 'b: ', b);
}

//swapNumb(2,3)

function scaleTheArray(arr, num){
  for (var i = 0; i < arr.length; i++){
    arr[i] = arr[i]* num;
  }
  console.log(arr);
}

//scaleTheArray(arr1, 2);

function onlyKeepLastFew(arr, x){
  for (var i = 0; i <= x; i++){
    arr.shift(i);
  }
  console.log(arr);
}

//onlyKeepLastFew(arr1, 2)
//done!

function mathHelp(M, B){
  X = (-B)/M
  console.log(X);
}

//mathHelp(1,2)

function poorKenny(spec){
    var i, j, table=[];
    for (i in spec) {
      // The constant 10 below should be computed based on the
      // weights in the spec for a correct and optimal table size.
      // E.g. the spec {0:0.999, 1:0.001} will break this impl.
      for (j=0; j<spec[i]*10; j++) {
        table.push(i);
      }
    }
    return function() {
      console.log(table[Math.floor(Math.random() * table.length)]);
    }
  }
  var rand012 = poorKenny({volcano:0.1, earthquake:0.2, blizzard:0.25, meteor_strike:.3});
  //rand012(); // random in distribution...

  function weightedRand2(spec) {
    var i, sum=0, r=Math.random();
    for (i in spec) {
      sum += spec[i];
      if (r <= sum) return i;
    }
  }
  weightedRand2({0:0.8, 1:0.1, 2:0.1});

function whatReallyHappened(){
  Math.random();
  if (Math.random() * 100 < 10){
    console.log('Volcano!');
  }
  if (Math.random() * 100 < 20){
    console.log('Earthquake!');
  }
  if (Math.random() * 100 < 25){
    console.log('Blizzard!');
  }
  if (Math.random() * 100 < 30){
    console.log('Meteor Strike!');
  }
}

//whatReallyHappened();

function soaringIQ(){
  var sum = 0;
  for (var i = 1; i <= 98; i++){
    sum += 0.01;
  }
  console.log(sum + 101);
}

//soaringIQ();

function letterGrade2(){
  var grade = '';

    var score = (prompt("Please enter Percent correct between 0 and 100: "));
    	if (score >= 90){
    		grade = "A";
      }
    	else if (score >= 80){
    		grade = "B";
      }
    	else if (score >= 70){
    		grade = "C";
      }
    	else if (score < 70){
    		grade = "D";
        }
  console.log("Score:" + score +  ": Your Grade is " + grade);
  console.log("End of program");
}

//letterGrade2();

function moreAccurateGrades(){
  var grade = '';

    var score = (prompt("Please enter Percent correct between 0 and 100: "));
    	if (score >= 90){
    		grade = "A";
      }
    	else if (score >= 80){
    		grade = "B";
      }
    	else if (score >= 70){
    		grade = "C";
      }
    	else if (score < 70){
    		grade = "D";
        }

  console.log("Score:" + score +  ": Your Grade is " + grade);
  console.log("End of program");
}
// still needs work....
