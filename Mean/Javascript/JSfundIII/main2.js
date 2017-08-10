function personMaker(name, quote){
  var person = {};
  person.name = name;
  person.quote = quote;
  person.distancetraveled = 0;
  person.say_name = function(){
    console.log(person.name);
    return person;
  };
  person.say_something = function(){
    console.log(person.name + ' says ' + person.quote);
    return person;
  };
  person.walk = function(){
    console.log(person.name + ' is walking');
    person.distancetraveled += 3;
    return person;
  };
  person.run = function(){
    console.log(person.name + ' is running');
    person.distancetraveled += 10;
    return person;
  };
  person.crawl = function(){
    console.log(person.name + ' is crawling');
    person.distancetraveled += 1;
    return person;
  };
}

function ninjaConstructor (name, cohort, beltlevel){
 var ninja = {};
 var belts = ['yellow', 'red', 'black'];
 ninja.name = name;
 ninja.cohort = cohort;
 ninja.beltLevel = 0;
 ninja.levelUp = function (){
   if (ninja.beltLevel < 2){
     ninja.beltLevel += 1;
     ninja.belt = belts[ninja.beltLevel];
   }
   return ninja;
 };
 ninja.belt = belts[ninja.beltLevel];
 return ninja;
}
