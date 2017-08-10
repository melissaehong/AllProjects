def even():
    for num in range (1, 1000):
        if (num % 2 == 1):
            print num

def multiple5():
    for num in range (5, 1000005):
        if (num % 5 == 0):
            print num

def sum():
    a = [1,2,5,10,255,3]
    sum = 0
    for num in a:
        sum += num
    print sum

def avg():
    sum = 0
    a = [1,2,5,10,255,3]
    for num in a:
        sum += num
        avg = sum/len(a)
    print avg

def oddeven():
    for x in range (1,2001):
        if (x % 2 == 0):
            oddeven = "even"
        elif (x % 2 == 1):
            oddeven = "odd"
        print "Number is {}.  This is an {} number.".format(x, oddeven)

a = [2,4,10,16]
def multiply(array, b):
    for x in range (len(array)):
        array[x] = array[x] * b
    return array

def scoreresults():
    scores = []
    for num in range(2):
        print "What is your score?"
        scores.append(input())

    print "Scores and Grades"

    for score in scores:
        if score in range (60, 69):
            grade = "D"
        elif score in range (70, 79):
            grade = "C"
        elif score in range (80, 89):
            grade = "B"
        elif score in range (90, 100):
            grade = "A"
        elif score < 60 or score > 101:
            print "Invalid input!"
            continue
        print ("Score: {}; Your grade is {}").format(score, grade)

    print "End of Program. Bye!"

def cointoss():
    heads = 0
    tails = 0
    import random
    import math
    print "Starting the program..."

    for x in range (1,5001):
        num = round(random.random())
        if num == 1:
            face = "head"
            heads += 1
        if num == 0:
            face = "tail"
            tails += 1

        print ("Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far").format(x, face, heads, tails)

    print "Ending the program. Thank you!"

x = [4,6,1,3,2,5,7,25]
def draw_stars(list):
    star = ''
    for value in list:
        for num in range(value):
            star += '*'
        print star

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars2(list):
    for x in list:
        star = ''
        if type(x) is int:
            for num in range(x):
                star += '*'
        elif type(x) is str:
            letter = x[0].lower()
            for num in range(len(x)):
                star += letter
        print star
def names():
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    for item in students:
        print '{} {}'.format(item['first_name'], item['last_name'])


users = {
'Students': [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'Melissa', 'last_name' : 'Hong'},
    {'first_name' : 'Salvador', 'last_name' : 'Cuevas'},
    {'first_name' : 'Sky', 'last_name' : 'Cuevas'}
],
'Instructors': [
    {'first_name': 'Michael', 'last_name': 'Choi'},
    {'first_name': 'Martin', 'last_name' : 'Puryear'}
]
}
def names2(dict):
    for key in dict:
        print key
        for i, user in enumerate(dict[key]):
            print "{} - {} {} - {}".format(i+1, user['first_name'], user['last_name'], len(user['first_name'] + (user['last_name'])))

import re
str = 'aaple'

if re.search(r"a.*a", str):
   print("That string had at least two 'a's in it!")
else:
   print("No more than one 'a' found!")

words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    print [word for word in words if re.search(r"v", word)]
    print [word for word in words if re.search(r"ss", word)]
    print [word for word in words if re.search(r"e$", word)]
    print [word for word in words if re.search(r"b.b", word)]
    print [word for word in words if re.search(r"b[a-z]+b", word)]
    print [word for word in words if re.search(r"b+\w+b", word)]
    print [word for word in words if re.search(r"aeiou", word)]
    print [word for word in words if re.search(r"r*e*g*u*l*a*r*e*x*p*r*e*s*s*i*o*n*", word)]
    print [word for word in words if re.search(r"\w\w", word)]
get_matching_words(words)
