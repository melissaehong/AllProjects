$(document).ready(function(){
  var customObject = {
    name: 'California, Eureka',
    onClick:function(p){
      console.log("I've been clicked Cali");
      console.log(p, "A bind me");
      console.log(this.name);
    }
  };
  console.log($('#test')[0]);
  var newObject = {
    name: "West Virginia, Montani semper liberi",
    onClick: function(para){
      console.log("I've been clicked now Virginia");
      console.log(para, "B Binded");
      console.log(this.name);
    }
  };

  var customObject2 = {
    name:'Alaska, Fairbanks',
    onClick:function(myParam){
      console.log("I've been clicked again Alaska");
      console.log(myParam, "C I've been passed by bind");
      console.log(this.name);
    }
  };

  $('button').click(customObject.onClick.bind(customObject, "1 Bind this argument!"));
  $('button').click(customObject.onClick.bind(customObject, "2 Now binding"));
  $('button').click(customObject.onClick.bind(customObject, "3 Finish binding"));
  $('button').click(customObject.onClick.bind(newObject, "4 Another bind"));
  $('button').click(customObject2.onClick.bind(customObject2, "5 bind this argument!"));
  $('button').click(customObject2.onClick.bind(customObject, "6 Bind this argument!"));
});

// 1. customObject binded to customObject this.name = Cal
// 2. ""
// 3. ''
// 4. customObject binded to newObject this.name = Virginia
// 5. customObject2 binded to customObject2 this.name = Alaska
// 6. customObject2 binded to customObject this.name = Cali


function levelUp(){
  console.log(this.name + ' has learned a new kata, in ' + this.gender + ' favorite langauge:' + this.language);
}

var person = {
  name: "Melissa",
  gender: 'her',
  language: 'JavaScript'
};

levelUp.call(person);
levelUp.apply(person);

function Ninja(name, age){
  this.name = name;
  this.age = age;
}

function BlackBelt(name, age){
  Ninja.call(this, name, age);
  this.belt = "black";
}

function YellowBelt(name, age){
  Ninja.apply(this,[name, age]);
  this.belt = 'yellow';
}

function Wizard(spell){
  this.spell = spell;
  this.cast = function(){
    console.log(this.spell);
  };
}

function GreenBelt(name, age, spell, cast){
  Ninja.apply(this, [name, age]);
  Wizard.call(this, spell, cast);
}

var yB = new YellowBelt('Melissa', 33);
var bB = new BlackBelt('Salvador', 34);
var gB = new GreenBelt('Sky', 3, 'charm');

console.log(bB.name);
console.log(yB.name);
console.log(gB.spell);
console.log(gB);
