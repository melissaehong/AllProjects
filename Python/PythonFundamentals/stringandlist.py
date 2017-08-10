str = "It's thanksgiving day. It's my birthday,too!"

print str.find('day')

print str.replace('day', 'month')

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]

print x[0], x[len(x)-1]


'''Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()

print x

firstx = x[0:len(x)/2]
secondx = x[len(x)/2:len(x)]

print firstx
print secondx

secondx.insert(0, firstx)

print secondx
