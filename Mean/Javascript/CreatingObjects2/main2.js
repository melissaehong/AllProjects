function VehicleConstructor(name, wheels, passengers, speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name, wheels, passengers, speed);
  }
  var distance_travelled = 0;
  var _this = this;
  function updateDistanceTravelled(){
    distance_travelled += _this.speed;
    console.log(distance_travelled);
  }
  this.name = name || 'unicycle';
  this.wheels = wheels || 1;
  this.passengers = passengers || 0;
  this.makeNoise = function(noise){
    noise = noise || 'Honk Honk';
    console.log(noise);
  };
  this.speed = speed;
  this.move = function(){
    this.makeNoise();
    updateDistanceTravelled();
  this.checkMiles = function(){
    console.log(distance_travelled);
  };
};
}

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
