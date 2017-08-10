//setting and swapping
var myNumber = 42;
var myName = 'Melissa';
var temp = myNumber;
myNumber = myName;
myName = temp;

//print -52 to 1066
for (var i = -52; i <= 1066; i++){
  console.log(i);
}

//don't worry, be happy
function beCheerful(n){
  for (var i = 1; i <=n; i++){
  console.log('good morning!');
 }
}

//multiples of three - but not all
for (var i = -300; i <= 0; i+=3){
  if (i === -3 || i === -6){
    continue;
  }
  console.log(i);
}

//printing integers with while
var i = 2000;
while (i <= 5280){
  console.log(i);
  i++;
}

//you say it's your birthday
function yourBirthday(a, b){
  if (a === 3 && b === 17 || a === 17 && b === 3){
    console.log("How did you know?");
  }
  else{
      console.log("Just another day...");
  }
}

//leap year
function leapYear(year){
  if (year % 4 === 0){
    leap = true;
    if (year % 100 === 0){
      leap = false;
      if(year % 400 === 0){
        leap = true;
      }
    }
  }
  else{
    leap = false;
  }
  return leap;
}

//print and count
var count = 0;
for (var i = 512; i <= 4096; i+=5){
  console.log("Number: " + i);
  count++;
  console.log("Count: " + count);
}
//multiples of six
var i = 6;
while (i <= 60000){
  console.log(i);
  i+=6;
}

//counting, the dojo way
for (var i = 1; i <= 100; i++){
  if (i%5 === 0){
    console.log('Coding ');
  }
  if (i%10 === 0){
    console.log('Dojo');
  }
}

//what do you know?
function know(incoming){
  console.log(incoming);
}

know('incoming')

//whoa, that sucker's huge
sum = 0;
for (var i = -300000; i <= 300000; i++) {
  if ( i%2 === 0) {
    sum += i;
  }
}
console.log(sum);

//countdown by fours
var i = 2016;
while (i > 0){
  console.log(i);
  i--;
}

//flexible countdown
function countDown(lowNum, highNum, mult){
  for (var i = highNum; i > lowNum; i -= mult){
    console.log(i);
  }
}

countDown(2,9,3)

//the final countdown
function finalCountdown(param1, param2, param3, param4){
  for (var i = param2; i < param3; i++){
    if(i === param4){
      continue;
    }
    if(i%param1 === 0){
      console.log(i);
    }
  }
}

finalCountdown(3,5,17,9);

function finalCountdown1(param1, param2, param3, param4){
  var i = param2;
  while (i < param3){
    i++;
    if(i === param4){
      continue;
    }
    else{
      if(i%param1 === 0){
      console.log(i);
    }
   }
  }
}

finalCountdown1(3,5,17,9)
