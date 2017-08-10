function runningLogger(){
  console.log('I am running!');
}

function multiplyByTen(numb){
  if (typeof(numb) == 'number'){
    return numb*10;
  }
}

console.log(multiplyByTen(5));

function stringReturnOne(){
  return 'cat';
}

function stringReturnTwo(){
  return 'dog';
}

console.log(stringReturnOne());
console.log(stringReturnTwo());


function caller(arg){
  if (typeof(arg) == 'function'){
    arg();
  }
}

caller(stringReturnOne());

function myDoubleConsoleLog(arg1, arg2){
  if (typeof(arg1) == 'function' && typeof(arg2) == 'function'){
    console.log(arg1(), arg2());
  }
}

myDoubleConsoleLog(stringReturnOne, stringReturnTwo);

function caller2(par1){
  console.log('starting');
  if (typeof(par1) == 'function'){
    setTimeout(function(){
        par1(stringReturnOne, stringReturnTwo);
        console.log('ending?');
        return 'interesting';
    }, 2000);
  }
}

caller2(myDoubleConsoleLog);

/*function caller3(param){
  console.log('starting');
  var x = setTimeout(function(){
    if (typeof(param) == 'function'){
      param(stringReturnOne, stringReturnTwo);
    }
  }, 2000);
  console.log('ending');
  return 'interesting';
}

caller3(myDoubleConsoleLog);
*/
