function fib(){
var a = 0, b = 1;
  function nacci(){
    var sum = a + b;
    console.log(sum);
    a = b; b = sum;
  }
  return nacci;
}
var fibCounter = fib();

fibCounter();
fibCounter();
fibCounter();
fibCounter();
fibCounter();
