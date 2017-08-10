// Hey Melissa -- It seems like you didn't test this code! I definitely recommend going back and at least writing the ninjaConstructor function.

function personConstructor(){
var person = {
  name: name,
  distance_traveled: 0,
  say_name: function (){
      console.log(person.name);
      },
  say_something: function(param){
      console.log(person.name + ' says ' + param);
    }, // need a comma
  // }, don't need this extra bracket
  /*
		Your walk, run and crawl seem to be doing ALMOST the same thing! Anyway you could move the logic into a single function?
		*/
  walk: function(){
    console.log(person.name + " is walking");
    person.distance_traveled += 3;
    console.log(person.name + " has traveled " + person.distance_traveled + " miles");
  },
  run: function(){
    console.log(person.name + " is running");
    person.distance_traveled += 10;
    console.log(person.name + " has traveled " + person.distance_traveled + " miles");
  },
  crawl: function(){
    console.log(person.name + " is crawling");
    person.distance_traveled += 1;
    console.log(person.name + " has traveled " + person.distance_traveled + " miles");
  }
}
return person;
}

/* Did you try running this code? I have a feeling that something like:

var person = personConstructor('Charlie');

might error...
*/

// Where's the ninjaConstructor??
