// print sum 1 to 5000
sum = 0;
for (var i = 1; i <= 5000; i++){
  if (i%2 === 1){
  sum += i;
  }
}
console.log(sum);

//iterating through an array

X = [1,3,5,7,9,13];

 for (var i = 0; i < X.length; i++){
   console.log(X[i]);
 }

 //max value

arr = [5,1,2,4,7]

max = arr[0]
 for (var i = 0; i < arr.length; i++){
   if (arr[i] > max){
     max = arr[i];
   }
 }
 console.log(max);
