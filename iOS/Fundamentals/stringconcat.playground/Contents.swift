//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"
str += " you are so cool"
print(str)

var name = "anakin"

print ("The maximum value \(Int.max)")

print ("The minimum value \(Int.min)")

print ("The maximum value \(Int32.max)")

print ("The minimum value \(Int32.min)")

print("The maximum value \(UInt32.max)")

print("The minimum value \(UInt32.min)")

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
