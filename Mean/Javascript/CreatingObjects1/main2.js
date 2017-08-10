function VehicleConstructor(name, wheels, passengers){
  var vehicle = {};
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers;
  vehicle.makeNoise = function(noise){
    console.log(noise);
  };
  return vehicle;
}

var Bike = VehicleConstructor('bike', 2, 1);
Bike.makeNoise = function(){
  console.log('ring ring');
};

var Sedan = VehicleConstructor('sedan', 4, 5);
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
