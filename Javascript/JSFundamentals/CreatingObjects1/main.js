function VehicleConstructor(name, wheels,passengers){
  var vehicle = {};
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers;
  vehicle.makeNoise = function(){
    console.log('beep-beep');
  };
  return vehicle;
}


var Bike = VehicleConstructor('bike',2);
Bike.makeNoise = function(){
  console.log('ring-ring');
};

var Sedan = VehicleConstructor('sedan', 4);
Sedan.makeNoise = function(){
  console.log('honk-honk');
};

var Bus = VehicleConstructor('bus', 4, 20);
Bus.pickup = function(passenger){
  Bus.passengers += passenger;
  return Bus;
};

console.log(Bike.name);
Sedan.makeNoise();
console.log(Bus.passengers);
Bus.pickup(2);
console.log(Bus.passengers);
