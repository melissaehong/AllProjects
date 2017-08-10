'''Assignment: Fun with Functions
Create a series of functions based on the below descriptions.

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:

Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.
Copy
Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:

a = [2,4,10,16]
Copy
Then:

b = multiply(a, 5)
print b
Copy
Should print [10, 20, 50, 80 ].

Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list. Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]'''

for num1 in range (1, 1001):
    if num1%2==0:
        evenodd = 'even', num1
        print "Number is " + str(num1) + '. This number is an even number.'
    else:
        evenodd = 'odd', num1
        print "Number is " + str(num1) + '. This number is an odd number.'


arr = []
def multiply(arr, num):
    for x in range(len(arr)):
        arr[x]*=num
    return arr


a = [2,4,10,16]

b = multiply(a, 5)
print b

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
