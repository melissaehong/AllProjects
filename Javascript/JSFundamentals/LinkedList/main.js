/* ********** Our Node Class **********
Generates a node for a singly linked list
parameters:
  val: a numerical value
private variables/functions:
  none:
public properties/methods:
  val: val;
  next: // another Node or null
  passThis: a function that passes a console log of this and self.
************** END **********   */
var Node = function(val){
  this.val = val;
  this.next = null;
};
Node.prototype.passThis = function(custom_return){
  console.log(this, "this");
  console.log(this.self, "self");
  console.log(custom_return, "My Return");
  return custom_return;
};
// ****************** END OF NODE ******************
/* ************* Singly Linked List Class (SingleList) *****************
Creates a simple singly linked list class with not too many methods yet!
parameters: none
private: none
public properties:
  head: first node in the List
public methods:
  add: adds a new node based on a value passed in. returns this
  dequeue: removes the head, and gives it to a callback, if a callback is passed. returns this
  remove_tail: removes the tail, and gives it to a callback as an argument, only if a callback is passed. returns this.
************** END **********   */
var SingleList= function(){
  this.head = null;
};
SingleList.prototype.add = function (val) {
  if (!this.head){
    this.head = new Node(val);
    return this;
  }
  var current = this.head;
  while(current.next){
    current = current.next;
  }
  current.next = new Node(val);
  return this;
};
SingleList.prototype.dequeue = function (callback) {
  var eliminatedNode = this.head;
  this.head = this.head.next;
  eliminatedNode.next = null;
  if (typeof(callback)=='function'){
    callback(eliminatedNode);
  }
  //console.log(this.head); optional
  return this;
};
// Write a remove tail! :)
// ************************ END OF LIST ************************
sList = new SingleList();
sList.add(1).add(2).add(3).add(4).head.next.passThis(sList).dequeue(
  function callback(myNode){
    console.log(myNode.val, "CHAINING INSANITY!");
  })
  .dequeue(
    function anotherCallback(myNode){
      console.log("******************************");
      console.log('Seriously, Stop!', myNode);
    });


    function Ninja(name){
      this.name = name;   // creating instance variables
      this.distance_traveled = 0;
    }
    // creating an instance method
    Ninja.prototype.walk = function() {
        console.log(this.name + ' is walking');
        this.distance_traveled += 1;
        return this;      // have this method return its own object
      };
    // creating an instance method
    Ninja.prototype.run = function() {
        console.log(this.name + ' is running');
        this.distance_traveled += 5;
        this.displayDistanceTraveled();
        return this;      // have this method return its own object
      };
    //another instance method
    Ninja.prototype.displayDistanceTraveled = function() {
        console.log('distance traveled: ', this.distance_traveled);
    };


    // creating instances/objects
    var ninja1 = new Ninja('Jay');
    var ninja2 = new Ninja('Michael');
    var ninja3 = new Ninja('Andrew');


    ninja1.walk().run().walk().run().run();  // because walk/run returns itself, we can chain these methods


    // you can also log ninja1 and study it
    console.log(ninja1);
