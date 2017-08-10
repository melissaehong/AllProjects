function VehicleConstructor(name, wheels, passengers, speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name, wheels, passengers, speed);
  }
  var characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  this.VIN = showVIN();
  function showVIN(){
    var vin = "";
    for (var i = 0; i < 17; i+=1){
      vin += characters[Math.floor(Math.random()*35)];
    }
    return vin;
  }

  this.distance_travelled = 0;
  this.speed = speed;
  this.name = name || 'unicycle';
  this.wheels = wheels || 1;
  this.passengers = passengers || 0;
}

  VehicleConstructor.prototype.makeNoise = function(noise){
    noise = noise || 'Honk Honk';
    console.log(noise);
    return this;
  };

  VehicleConstructor.prototype.updateDistanceTravelled = function(){
    this.distance_travelled += this.speed;
    console.log(this.distance_travelled);
    return this;
  };

  VehicleConstructor.prototype.move = function(){
    this.makeNoise();
    this.updateDistanceTravelled();
    return this;
  };

  VehicleConstructor.prototype.checkMiles = function(){
    console.log(this.distance_travelled);
    return this;
  };



var Bike = new VehicleConstructor('bike', 2, 1);
Bike.makeNoise = function(){
  console.log('ring ring');
};

var Sedan = new VehicleConstructor('sedan', 4, 5);
Sedan.makeNoise = function(){
  console.log('Honk Honk!');
};

var Bus = VehicleConstructor('bus', 4, 20);
Bus.pickUp = function(passengerCount){
  Bus.passengers += passengerCount;
  return Bus;
};


Bike.makeNoise();
Sedan.makeNoise();
console.log(Bus.passengers);
Bus.pickUp(5);
console.log(Bus.passengers);

console.log('hi');

var car = new VehicleConstructor('car', 4, 2, 40);
car.move();
car.checkMiles();
console.log(car.speed);

car.move().checkMiles().updateDistanceTravelled();
console.log(car.VIN);

function getRandomA(min, max){
  return Math.floor(Math.random()* (max - min)) + min;
}
console.log(getRandomA(1, 5));
