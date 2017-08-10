function VehicleConstructor(name, wheels, passengers, speed){
  this.name = name;
  this.wheels = wheels;
  this.passengers = passengers;
  this.speed = speed;
  this.distance_traveled = 0;
  var chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  this.vin = getRandom();
  function getRandom(){
    random = '';
    for (var i = 0; i<17; i++){
    random+=chars[Math.floor(Math.random()*35)];
    }
    return random;
  }
  }

  VehicleConstructor.prototype.updateDistanceTraveled = function(){
    this.distance_traveled += this.speed;
  };
  VehicleConstructor.prototype.makeNoise = function(){
    console.log('beep-beep');
  };
  VehicleConstructor.prototype.move = function(){
    this.updateDistanceTraveled();
    this.makeNoise();
  };
  VehicleConstructor.prototype.checkMiles = function(){
    console.log(this.distance_traveled);
  };

bike = new VehicleConstructor('bike',2, 1, 10);
bike.makeNoise = 'ring-ring';

sedan = new VehicleConstructor('sedan', 4, 1, 40);
sedan.makeNoise = 'honk-honk';

bus = new VehicleConstructor('bus', 4, 20, 20);
bus.pickup = function(passenger){
  bus.passengers += passenger;
  return;
};

bus.checkMiles();
bus.move();
bus.checkMiles();
console.log(bus.vin);
console.log(bus.vin);
