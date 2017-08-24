// stack.js
var Stack = (function(){
  function Stack() {
    this.dataStore = [];
    this.top = 0;
  }
  Stack.prototype.push = function(item) {
    this.top = this.top + 1;
    this.dataStore[this.top] = item;
    return this;
  };
  Stack.prototype.pop = function() {
    // your code here
    this.top = this.top-1;
    return this;
  };
  Stack.prototype.display = function() {
    for (var i = 1; i < this.dataStore.length; i++){
      console.log(this.dataStore[i]);
    }
  };
  return Stack;
})();
module.exports = Stack;
