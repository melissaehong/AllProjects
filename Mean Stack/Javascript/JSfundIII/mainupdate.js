function personConstructor(name){
var person = {
  name: name,
  distance_traveled: 0,
  say_travel : function(){
    console.log(person.name + " has traveled " + person.distance_traveled + " miles");},
  say_name: function (){
      console.log(person.name);
      },
  say_something: function(param){
      console.log(person.name + ' says ' + param);
  },
  walk: function(){
    console.log(person.name + " is walking");
    person.distance_traveled += 3;
    person.say_travel();
  },
  run: function(){
    console.log(person.name + " is running");
    person.distance_traveled += 10;
    person.say_travel();
  },
  crawl: function(){
    console.log(person.name + " is crawling");
    person.distance_traveled += 1;
    person.say_travel();
  }
};
return person;
}

var Melissa = personConstructor('Melissa');
console.log(Melissa.name);
Melissa.say_travel();
Melissa.say_name();
Melissa.say_something('I am cool');
Melissa.walk();
Melissa.run();
Melissa.crawl();

function ninjaConstructor(name, cohort){
  var ninja = {};
  var belts = ['yellow','red', 'black'];
    ninja.name = name;
    ninja.cohort = cohort;
    ninja.beltlevel = belts[0];
    ninja.levelup = function (){
      for (var i = 0; i < belts.length; i ++){
        if (ninja.beltlevel === 'yellow'){
          ninja.beltlevel = belts[1];
          return;
        }
        if (ninja.beltlevel === 'red'){
          ninja.beltlevel = belts[2];
          return;
        }
      }
    };
  return ninja;
}

var Melissa2 = ninjaConstructor('Melissa', 'July');
console.log(Melissa2.name);
console.log(Melissa2.cohort);
console.log(Melissa2.beltlevel);
Melissa2.levelup();
console.log(Melissa2.beltlevel);
Melissa2.levelup();
console.log(Melissa2.beltlevel);
