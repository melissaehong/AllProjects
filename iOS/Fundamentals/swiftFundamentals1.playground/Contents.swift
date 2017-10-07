//: Playground - noun: a place where people can play

import UIKit

var type: Float = "Rectangle"
var description: String = "A quadrilateral with four right angles"
let width: Double = 5
let height: Int = 10.5
var area: Double = width * height
height += 1
width += 1
area = width * height
// Note how you can "interpolate" variables into Strings using the following syntax
print("The shape is a \(type) or \(description) with an area of \(area)")
