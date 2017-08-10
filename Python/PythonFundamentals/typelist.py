'''Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

#input

#output
"The array you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
Copy
# input
l = [2,3,1,7,4,12]
#output
"The array you entered is of integer type"
"Sum: 29"
Copy
# input
l = ['magical','unicorns']
#output
"The array you entered is of string type"
"String: magical unicorns"'''

l = ['magical','unicorns', 'hi']
l = [2,3,1,7,4,12]
l = [2,'hi', 3,1, 'welcome', 7,4,12]

sum = 0
string1 = ''
message = ''
for element in l:
    if isinstance (element, str):
        message = 'string'
        string1 += element
    if isinstance(element, (int or float)):
        sum += element
        message = 'integer'

print "The array you entered is of " + message + ' type'
if message == 'string':
    print "String: " + str(string1)
if message == 'integer':
    print "Sum: " + str(sum)
if message == 'string' and 'integer':
    print "String: " + str(string1)
    print "Sum: " + str(sum)
