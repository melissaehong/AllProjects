P = [];

function randomArray(X){
  for (var i = 1; i <= 10; i++){
  X.push(Math.floor(Math.random()*101));
  }
console.log(X);
}

randomArray(P);
