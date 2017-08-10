function itemCounter(obj){
  var counterObj = {
      properties: 0,
      methods: 0
    }

  for (key in obj) {
    if (typeof obj[key] === "function") {
      counterObj.methods += 1;
    } else {
      counterObj.properties += 1;
    }
  }
  return counterObj;
}
