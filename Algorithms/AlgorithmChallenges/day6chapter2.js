function rockinDojo(num){
  var cost;
  if (num === 1){
    cost = 20;
  }
  if (num === 2){
    cost = Math.ceil(20 * 0.91);
  }
  if (num === 3){
    cost = Math.ceil(20 * 0.81);
  }
  if (num >= 4){
    cost = Math.ceil(20 * 0.65);
  }
  console.log(cost);
}

//rockinDojo(1);
//rockinDojo(2);
//rockinDojo(3);
//rockinDojo(4);


//done!!
function clockHandAngles2(){
  //come back later...
}

function extractOMatic(num, digitNum){
  for (var i = 0; i <= num; i++){
    if (i === digitNum){
      var powerNum = Math.pow(10, i);
      var answerPlace = num / powerNum;
      answer = Math.floor(answerPlace % 10);
    }
  }
  console.log(answer);
}

//extractOMatic(1824, 2);
//extractOMatic(1824, 7);
//extractOMatic(1824, 0);

function mostSignificantDigit(num){

}

function gamingFun(){

}

function rollOne(){
  return Math.ceil(Math.random()*6);
}

function playFives(num){
  for (var i = 1; i <= num; i++){
    x = rollOne();
    console.log(x);
    if (x === 5){
      console.log("That's good luck!")
    }
    }
}

function playStatistics(){
  var arr = [];
  for (var i = 1; i <= 8; i++){
    x = rollOne();
    arr.push(x);
  }
  var max = arr[0];
  var min = arr[0];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
    if (arr[i] > max){
      max = arr[i];
    }
  }
    console.log("Min: " + min);
    console.log("Max: " + max);
    return arr;
}

//playStatistics();

function playStatistics2(){
  var arr = [];
  for (var i = 1; i <= 8; i++){
    x = rollOne();
    arr.push(x);
  }
  var max = arr[0];
  var min = arr[0];
  var sum = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
    if (arr[i] > max){
      max = arr[i];
    }
    sum += arr[i];
  }
    console.log("Min: " + min);
    console.log("Max: " + max);
    console.log("Sum: " + sum/arr.length);
}

//playStatistics2();

function playStatistics3(num){
  var arr = [];
  for (var i = 1; i <= num; i++){
    x = rollOne();
    arr.push(x);
  }
  var max = arr[0];
  var min = arr[0];
  var sum = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
    if (arr[i] > max){
      max = arr[i];
    }
    sum += arr[i];
  }
    console.log("Min: " + min);
    console.log("Max: " + max);
    console.log("Sum: " + sum/arr.length);
}

//playStatistics3(100);

function playStatistics3(num){
  var arr = [];
  for (var i = 1; i <= num; i++){
    x = rollOne();
    arr.push(x);
  }
  var max = arr[0];
  var min = arr[0];
  var avgRoll = 0;
  var oneCount = 0;
  var twoCount = 0;
  var threeCount = 0;
  var fourCount = 0;
  var fiveCount = 0;
  var sixCount = 0;
  var arr2 = [];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
    if (arr[i] > max){
      max = arr[i];
    }
    if (arr[i] === 1){
      oneCount++;
    }
    if (arr[i] === 2){
      twoCount ++;
    }
    if (arr[i] === 3){
      threeCount++;
    }
    if (arr[i] === 4){
      fourCount++;
    }
    if (arr[i] === 5){
      fiveCount++;
    }
    if (arr[i] === 6){
      sixCount++;
    }
  }
  arr2.push(oneCount);
  arr2.push(twoCount);
  arr2.push(threeCount);
  arr2.push(fourCount);
  arr2.push(fiveCount);
  arr2.push(sixCount);
  console.log("Average Numbers: " + arr2);
  var max2 = arr2[0];
  var maxIndex = 0;
    for (var j = 0; j < arr2.length; j++){
      if (arr2[j] > max2){
        max2 = arr2[j];
        maxIndex = j;
      }
    }
    console.log("Max Number Count: " + max2);
    console.log("Max Index Value:" + (maxIndex +1))
  }


//playStatistics3(300);

function statisticsUntilDoubles(num){
  var answer = []
  var findFirstDup = {}
  for (var i = 0; i < num; i++){
      answer.push(Math.ceil(Math.random()*20));
  }
  console.log(answer);
  var min = answer[0];
  var max = answer[0];
  var sum = 0;
  for (var i = 0; i < answer.length; i++){
    if (answer[i] < min){
      min = answer[i];
    }
    if (answer[i] > max){
      max = answer[i];
    }
    sum += answer[i];
  }
  console.log("Number of rolls: " + num)
  console.log("Min: " + min);
  console.log("Max: " + max);
  console.log("Avg: " + sum/answer.length);
  for (var i of answer) {
    if (findFirstDup[i]) return console.log( "First duplicate: " + i);
    findFirstDup[i] = i;
  }
}
//number of rolls
// min
// max
// avg
//randomly returns integers between 1 and 20 inclusive

//statisticsUntilDoubles(20)

// done!!

x = 10;
y = 5;

function xLocation(){
  console.log(x);
}

function yLocation(){
  console.log(y);
}

function moveBy(xOffset, yOffset){
  x += xOffset;
  y += yOffset;
  return (x, y);
}

function reset(){
  x = 0;
  y = 0;
}

/*reset();
xLocation();
yLocation();
moveBy(1,-2);
moveBy(3,1);
xLocation();
yLocation();
*/

//date on a deserted island
function weekdayName(weekdayNum){
  // getting day of the week based on numbers 1 to 6; number 1 starting with "Sunday" and number 6 ending with "Saturday"
  switch (weekdayNum){
    case 1:
      console.log("Sunday");
      break;
    case 2:
      console.log("Monday")
      break;
    case 3:
      console.log("Tuesday")
      break;
    case 4:
      console.log("Wednesday")
      break;
    case 5:
      console.log("Thursday")
      break;
    case 6:
      console.log("Friday")
      break;
    case 7:
      console.log("Saturday");
      break;
  }
}

function weekdayName2(weekdayNum){
  // getting days of the week based on 365 days, starting with 1 = "Sunday" and 6 = "Saturday"
  while (weekdayNum > 7){
    (weekdayNum %= 7);
  }
  weekdayNum = Math.floor(weekdayNum);

  switch (weekdayNum){
    case 0:
      console.log("Saturday");
      break;
    case 1:
      console.log("Sunday");
      break;
    case 2:
      console.log("Monday")
      break;
    case 3:
      console.log("Tuesday")
      break;
    case 4:
      console.log("Wednesday")
      break;
    case 5:
      console.log("Thursday")
      break;
    case 6:
      console.log("Friday")
      break;
    case 7:
      console.log("Saturday");
      break;
  }
}

function someDays(){
  for (var i = 0; i < 17; i ++){
  dayNum = Math.floor(Math.random()*366);
    x = weekdayName2(dayNum);
    if (x === "Sunday"){
      console.log("Enjoy your day off!")
    }
  }
}

someDays();

function monthName(monthNum){

}

function dayToMonth(dayNum){

}

function fullDate(dayNum){

}

function fullDate2(dayNum){

}

function fullDate3(dayNum){

}
