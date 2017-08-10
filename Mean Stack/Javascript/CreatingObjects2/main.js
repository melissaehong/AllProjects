function VehicleConstructor(name, wheels, passengers, speed){
  var distance_traveled = 0;
  var updateDistanceTraveled = function(){
    distance_traveled += speed;
  }
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.speed = speed;
  this.makeNoise = function(){
    console.log('beep-beep');
  }
  this.move = function(){
    updateDistanceTraveled();
    this.makeNoise();
  }
  this.checkMiles = function(){
    console.log(distance_traveled);
  }
}

var Bike = new VehicleConstructor('bike',2, 1, 10);
Bike.makeNoise = 'ring-ring';

var Sedan = new VehicleConstructor('sedan', 4, 1, 40);
Sedan.makeNoise = 'honk-honk';

var Bus = new VehicleConstructor('bus', 4, 20, 20);
Bus.pickup = function(passenger){
  Bus.passengers += passenger;
  return;
}

Bus.checkMiles();
Bus.move();
Bus.checkMiles();
