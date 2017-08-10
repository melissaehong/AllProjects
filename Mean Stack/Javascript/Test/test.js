console.log('hello!');
console.log('hi');

console.log(a);
var a = "weird";
// Will it throw an error?  What will it print, if it doesn't throw an error?
// How about this?
console.log(typeof(b));
var b = "weird too";
console.log(typeof(b));

var arr = [3, 6];
arr[234] = "hi";
//
console.log( arr.length ); // 235
console.log( arr[34] ); // undefined
arr.length = 3;
console.log( arr[34] );
console.log( arr[234] );
console.log( arr.length );
arr.length = 500;
console.log( arr[234] );
console.log( arr.length );
