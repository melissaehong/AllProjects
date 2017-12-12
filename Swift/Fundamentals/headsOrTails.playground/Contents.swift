//: Playground - noun: a place where people can play

import UIKit

/*Create a function tossCoin() -> String
Have this function print "Tossing a Coin!"
Next have the function randomly pick either "Heads" or "Tails"
Have the function print the result
Finally, have the function return the result
Now create another function tossMultipleCoins(Int) -> Double
Have this function call the tossCoin function multiple times based on the Integer input
Have the function return a Double that reflects the ratio of head toss to total toss*/

func tossCoin() -> String{
    var result: String
    print("Tossing a Coin!")
    if arc4random_uniform(2) == 0 {
        result = "Heads"
    }
    else{
        result = "Tails"
    }
    print(result)
    return result
}

tossCoin()

/*func tossMultipleCoins(tosses:Int) -> Double{
    var headsCount = 0
    var tailsCount = 0
    
    for _ in 0...tosses{
        if tossCoin() == "Heads"{
            headsCount += 1
        }
        else{
            tailsCount += 1
        }
    }
    
    let ratio = Double(tosses) / Double(headsCount)
    print(ratio)
    return ratio
    
}


tossMultipleCoins(tosses:5)
print("hello")
tossMultipleCoins(tosses: 13)
print("end")
 */

