console.log('I am running from node');
console.log("hello");

var myarr = [1,5,25,125, 42];

for (var index in myarr){
  console.log(myarr[index]*5);
}

for (var i = 0; i < myarr.length; i++){
  console.log(myarr[i]*5)
}

var myobject = {
  language: "Javascript",
  dojo: "Washington DC",
  favorite_instructor: "Me"
};


Object.keys(myobject).forEach(function(key,value){
  console.log(key, myobject[key]);
});

for (var key in myobject){
  console.log(key, myobject[key] + " the value");
}
