var x = [3,5, "Dojo", "rocks", "Michael", "Sensei"];
console.log(x);

for (var i = 0; i < x.length; i++){
  console.log(x[i]);
}

x.push(100);
console.log(x);
for (var i = 0; i < x.length; i++){
  console.log(x[i]);
}

x.push(['hello', 'world', 'javascript is fun']);
console.log(x);

for (var i = 0; i < x.length; i++){
  console.log(x[i]);
}

var sum = 0;
for (var i = 1; i <=500; i++){
  sum+=i;
}
console.log(sum);


var array = [1, 5, 90, 25, -3, 0];
var min = array[0];
for (var i = 1; i<array.length; i++){
  if (array[i] < min){
    min = array[i];
  }
}
console.log(min);

var sum = array[0];
for (var i = 1; i < array.length; i++){
  sum += array[i];
}
console.log(sum/array.length);

var newNinja = {
  name: 'Jessica',
  profession: 'coder',
  favorite_language: 'Javascript',
  dojo: 'Dallas'
};

for (var key in newNinja){
  console.log(key + ' : ' + newNinja[key]);
}
