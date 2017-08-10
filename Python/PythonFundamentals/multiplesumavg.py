'''Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]'''

'''for x in range(1,1001, 2):
    print x

for x in range(5,1000000, 5):
    print x'''

a = [1, 2, 5, 10, 255, 3]

sum = 0
for element in a:
    sum+=element
print sum

sum = 0
for element in a:
    sum+=element
avg = sum/len(a)
print avg
