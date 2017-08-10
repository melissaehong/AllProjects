'''Assignment: Compare Arrays
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
Copy
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
Copy
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
Copy
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
'''

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
answer = ''

for element in list_one:
    for element in list_two:
        if list_one == list_two:
            answer = 'same'
        if list_one != list_two:
            answer = 'not same'

if answer == 'same':
    print "lists are the same"

if answer == 'not same':
    print 'lists are not the same'
