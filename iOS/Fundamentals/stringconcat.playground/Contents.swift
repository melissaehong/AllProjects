//: Playground - noun: a place where people can play

import UIKit

/*var str = "Hello, playground"
str += " you are so cool"
print(str)

var name = "anakin"

print ("The maximum value \(Int.max)")

print ("The minimum value \(Int.min)")

print ("The maximum value \(Int32.max)")

print ("The minimum value \(Int32.min)")

print("The maximum value \(UInt32.max)")





;./'}
\\ \int("The minimum value \(UInt32.min)")

var Poem = "Alive without breath,As cold as death;Never thirsty, ever drinking,All in mail never clinking."
//This can be reformatted with triple-quotes to allow multiple lines!
Poem = """
Alive without breath,
As cold as death;
Never thirsty, ever drinking,
All in mail never clinking.
"""
print(Poem)

var arrayOfInts = [1, 2, 3, 4, 5]
var popped = arrayOfInts.remove(at: 0)
print(popped)
print(arrayOfInts)

var myInt = 1
func changeMyInt(someInt: inout Int) {         // must specify "inout"
    someInt = someInt + 1
    print(someInt)
}
changeMyInt(someInt: &myInt)                            // must pass in the variable with "&" symbol
print(myInt)

func sayHello(name: String = "buddy") -> String {
    return "Hey \(name)"
}
var greeting: String?
greeting = sayHello()
print(greeting)

func calculateAreaOfRectangleWithWidth(w: Int, andHeight h: Int) -> Int {
    return w * h
}
var area = calculateAreaOfRectangleWithWidth(w: 10, andHeight: 3)
print(area)
*/
func lookForSomethingIn(dictionary: [String: Int], forKey key: String) -> Int? {
    if let value = dictionary[key] {
        return value
    } else {
        return nil
    }
}
var jerseyNumbers = ["Kobe": 24, "Curry": 30]
var jerseyNumber = lookForSomethingIn(dictionary: jerseyNumbers, forKey: "Kobe")
if let num = jerseyNumber {
    print(num)
}

var present: String? = "Apple Watch"
// If we can let "unwrappedPresent" equal "present" meaning there is something inside of present then go on to do something with "unwrappedPresent"
if let unwrappedPresent = present {
    print("OMG THANK YOU FOR THE \(unwrappedPresent)")
}
