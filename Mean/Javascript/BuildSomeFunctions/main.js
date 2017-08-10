function runningLogger(){
  console.log('I am running!');
}

function multiplyByTen(parameter1){
  console.log(parameter1*10);
}

multiplyByTen(5);

function stringReturnOne(){
  console.log('I am a string!')
}

stringReturnOne();

function stringReturnTwo(){
  console.log('I am a string too!')
}

stringReturnTwo();

function caller(parameter1){
  if (typeof parameter1 === 'function'){
    parameter1.call;
  }
}

caller(stringReturnOne());

function myDoubleConsoleLog(param1, param2){
  if (typeof param1 === 'function'){
    console.log(param1);
  }
  if (typeof param2 === 'function'){
    console.log(param2);
  }
}

myDoubleConsoleLog(multiplyByTen(3), runningLogger());

function caller2(param1){
  console.log('starting');
  if (typeof param1 === 'function'){
    setTimeout(function(){
      console.log(param1);
      console.log('ending?');
      return 'interesting';
    }, 2000);
  }
}

caller2(myDoubleConsoleLog);
