//: Playground - noun: a place where people can play

import UIKit

/*Write a program that adds the numbers 1-255 to an array
Swap two random values in the array
Hint: you can use the arc4random_uniform(UInt32) function to get a random number from 0 to the number passed in. The arc4random_uniform function takes in one parameter that is of the UInt32 type and returns a random number that is of the UInt32 type. How can you deal with this using your knowledge of types?
Now write the code that swaps random values 100 times (You've created a "Shuffle"!)
Remove the value "42" from the array and Print "We found the answer to the Ultimate Question of Life, the Universe, and Everything at index __" and print the index of where "42" was before you removed it.
*/
var array = [Int]()

for i in 1...255 {
    array.append(i)
}

//Exercise 2

var length = array.count


var randNumberOne = Int(arc4random_uniform(UInt32(length)))
var randNumberTwo = Int(arc4random_uniform(UInt32(length)))

print(randNumberOne)


print(array)

for _ in 1...100{
    let randNumberOne = Int(arc4random_uniform(UInt32(length)))
    let randNumberTwo = Int(arc4random_uniform(UInt32(length)))
    
    if randNumberOne != randNumberTwo{
        array.swapAt(randNumberOne, randNumberTwo)
    }
}

print(array)

for i in 0..<array.count {

    if(array[i] == 42){
        
        array.remove(at: i)
        
        print("We found the answer to the Ultimate Question of Life, the Universe, and Everything at index \(i)")
        
        break
    }
}

