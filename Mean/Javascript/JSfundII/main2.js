function summing(x,y){
  var sum = 0;
  for (var i = x; i <=y; i++){
  sum+=i;
}
console.log(sum);
}

summing(1,100);
summing(2,40);

function minArray(arr){
  var min = arr[0];
for (var i = 1; i<arr.length; i++){
  if (arr[i] < min){
    min = arr[i];
  }
}
console.log(min);
}

minArray([4,1,10]);
minArray([-3, -100, 100]);

function avg(arr1){
var sum = arr1[0];
for (var i = 1; i < arr1.length; i++){
  sum += arr1[i];
}
console.log(sum/arr1.length);
}

avg([1,2,3,4]);
avg([5,6,7,8]);

var myObject = {
  summing: function(x,y){
    var sum = 0;
    for (var i = x; i <=y; i++){
    sum+=i;
  }
  console.log(sum);
},

  minArray: function(arr){
    var min = arr[0];
  for (var i = 1; i<arr.length; i++){
    if (arr[i] < min){
      min = arr[i];
    }
  }
  console.log(min);
},

  avg: function(arr1){
  var sum = arr1[0];
  for (var i = 1; i < arr1.length; i++){
    sum += arr1[i];
  }
  console.log(sum/arr1.length);
  }
};

var person = {
  name: "Melissa",
  distance_traveled: 0,
  say_name: function(){
    console.log(person.name);
  },
  say_something: function(quote){
    console.log(`${person.name} says ${quote}`);
    console.log(person.name + ' says ' + quote);
  },
  walk: function(){
    console.log(person.name + ' is walking');
    person.distance_traveled += 3;
    return person;
  },
  run: function(){
    console.log(person.name + ' is running');
    person.distance_traveled += 10;
    return person;
  },
  crawl: function(){
    console.log(person.name + ' is crawling');
    person.distance_traveled += 1;
    return person;
  },
  chewGum: function(){
    console.log("I can walk and chew gum, but I can't chew gum and walk");
    return person;
  }
};

person.walk().chewGum();
person.say_something("hi");
person.chewGum().walk();
