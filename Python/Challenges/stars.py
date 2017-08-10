<<<<<<< Updated upstream
'''Part 1
Create a function called  draw_stars() that takes a list of numbers and prints out  *.

For example:
=======
'''For example:
>>>>>>> Stashed changes

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x) should print the following in when invoked:

****
******
*
***
*****
*******
*************************
'''
<<<<<<< Updated upstream
x = [4,6,1,3,5,7,25]
def stars(num_list):
	for num in num_list:
		output = ''
		for i in range (num):
			output += '*'
		print output

stars(x)

y = [4, "Tom", 1, "Michael", 5, 6, "Jimmy Smith"]
def stars2(random_list):
	for item in random_list:
		output = ''
		if type(item) is int:
			for i in range(item):
				output += '*'
		elif type(item) is str:
			first_letter = item[0].lower()
			for i in range (len(item)):
				output += first_letter
		print output

stars2(y)
=======
x = '*'
print x

x = 2
if x == 2:
	x = '**'
	print x

x = 1, 2
for x in range (0, 4):
	if x == 1:
		x = '*'
		print x
	if x == 2:
		x = '**'
		print x

 print "hello"
>>>>>>> Stashed changes
