import random

def coin_toss(repetition):
    print 'Starting the program...'
    face = ''
    head_count = 0
    tail_count = 0
    num = 1
    for x in range (1, repetition):
        coin = round(random.randint(0,1))
        if coin == 0:
            face = 'head'
            head_count+=1
            print "Attempt # " + str(num) + ": Throwing a coin...  It's a " + str(face) + '! Got ' + str(head_count) + ' head(s) so far and ' + str(tail_count) + ' tails(s) so far'
        if coin == 1:
            face = 'tails'
            tail_count+=1
            print "Attempt # " + str(num) + ": Throwing a coin...  It's a " + str(face) + '! Got ' + str(head_count) + ' head(s) so far and ' + str(tail_count) + ' tails(s) so far'
        num += 1

coin_toss(100)
