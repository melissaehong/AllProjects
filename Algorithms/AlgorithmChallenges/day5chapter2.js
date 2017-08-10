function print1to255(){
   for (var i = 1; i <= 255; i++){
     console.log(i);
   }
}

function printIntsAndSum(){
  sum = 0;
  for (var i = 0; i <= 255; i++){
    console.log(i);
    sum += i;
    console.log(sum);
  }
}

function findPrintMax(arr){
  var max = arr[0];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > max){
      max = arr[i];
    }
  }
  console.log(max);
}

function arrayWithOdds(arr){
  for (var i = 1; i <= 255; i++){
    arr.push(i);
  }
  console.log(arr);
}

function greaterThanY(arr, Y){
  var count = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > Y){
      count++;
    }
  }
  console.log(count);
}

function maxMinAverage(arr){
  max = arr[0];
  min = arr[0];
  sum = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
    if (arr[i] > max){
      max = arr[i];
    }
    sum += i;
  }
  var avg = sum/arr.length;
  console.log(max, min, avg);
}

function swapStringNegative(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < 0){
      arr[i] = 'Dojo';
    }
  }
  console.log(arr);
}

function printOdds1to255(){
  for (var i = 1; i <= 255; i+=2)
  console.log(i);
}

function iteratePrintArray(arr){
  for (var i = 0; i <= arr.length; i++){
    console.log(i);
  }
}

function getPrintAverage(arr){
  sum = 0;
  for (var i = 0; i < arr.length; i++){
    sum += i;
  }
  var avg = sum/arr.length;
  console.log(avg);
}

function squareValues(arr){
  for (var i = 0; i < arr.length; i++){
    arr[i] = arr[i]*arr[i];
  }
  console.log(arr);
}

function zeroOutNeg(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < 0){
      arr[i] = 0;
    }
  }
  console.log(arr);
}

arr1 = [0,2,4,6];
function shiftArrayValues(arr){
  for (var i = 0; i < arr.length-1; i++){
      arr[i] = arr[i+1];
    }
  arr[arr.length-1] = 0;
  console.log(arr);
}

//shiftArrayValues(arr1);

function sigma(num){
  sum = 0;
  for (var i = 1; i <= num; i++){
    sum += i;
  }
  console.log(sum);
}

//sigma(4);

function factorial(num){
  var multi = 1;
  for (var i = 1; i <= num; i++){
    multi *= i;
  }
  console.log(multi);
}

//factorial(5);
x = [];

function drawLeftStars(num){
  if (num <= 75){
    for (var i = 0; i <= num; i++){
      output = ''
      for (var j = 0; j < i; j++){
        output += '*';
      }
    }
  }
  else{
    return console.log('Too big!');
  }
  console.log(output);
}

//drawLeftStars(4);
//drawLeftStars(88);

function drawRightStars(num){
  for (var i = 0; i <= num; i++){
    var output = ' ';
    for (var k = 0; k < 75-num; k++){
      output += ' ';
    }
    for (var j = 0; j < i; j++){
      output += '*';
    }
  }
  console.log(output);
}

//drawRightStars(3);

function drawCenteredStars(num){
for (var i = 0; i <= num; i++){
  var output = ' ';
  for (var k = 0; k < (75-num)/2; k++){
    output += ' ';
  }
  for (var j = 0; j < i; j++){
    output += '*';
    }
  for (var l = 0; l < (75-num)/2; l++){
    output += ' ';
  }
  }
  console.log(output);
}
//drawCenteredStars(3);

function drawRightChars(num, char){
  for (var i = 0; i <= num; i++){
    output = ' '
    for (var k = 0; k < 75-num; k++){
      output += ' '
  }
    for (var j = 0; j < i; j++){
      output += char;
    }
  }
  console.log(output)
}

//drawRightChars(9, 'k');

function threesAndFives(){
  sum = 0;
  for (var i = 100; i <= 400; i ++){
    if (i%3 === 0 && i%5 === 0){
      continue;
    }
    if (i%3 === 0 || i%5 === 0) {
      sum += i;
    }
  }
  console.log(sum);
}

//threesAndFives();

function generateCoinChange(cents){
    quarters = Math.floor(cents/25);
    cents = cents % 25;

    dimes = Math.floor(cents/10);
    cents = cents % 10;

    nickels = Math.floor(cents/5);
    cents = cents % 5;

    pennies = cents;

  console.log('quarters: ' + quarters);
  console.log('dimes: ' + dimes);
  console.log('nickels: ' + nickels);
  console.log('pennies: ' + pennies);
}

//generateCoinChange(94);

function messayMathMashup(num){
  sum = 0;
  for (var count = 0; count <= num; count++){
    if (count%3 === 0){
      continue;
    }
    if (count === num*(1/3)){
      return console.log(-1);
    }
    if (count%7 === 0){
      add = count*2;
      sum += add;
    }
    else{
    sum += count;
  }
  }
  console.log(sum);
}

//messayMathMashup(4);

function twelveBarBlues(){

}

function fibonacci(){

}

function sumOneDigit(){

}

function clockHandAngles(){

}

function isPrime(){

}
