import random, math

def grade(repetition):
    print "Scores and Grades"
    for x in range(0, repetition):
        score = math.floor(random.random()*100)
        if score >= 90:
            print 'Your score is: ' + str(score) + '; Your grade is A'
        if score >= 80 and score <= 89:
            print 'Your score is: ' + str(score) + '; Your grade is B'
        if score >= 70 and score <= 79:
            print 'Your score is: ' + str(score) + '; Your grade is C'
        if score >= 60 and score <= 69:
            print 'Your score is: ' + str(score) + '; Your grade is D'
        if score >= 0 and score <= 59:
            print 'Your score is: ' + str(score) + '; Your grade is F'
    print "End of Program. Bye!"

grade(10)
