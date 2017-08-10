score_list=[]

for num in range(2):
	score_list.append( input("Please enter percent correct:"))

for score in score_list:
	if score in range (90, 100):
		grade = "A"
	elif score in range (80, 89):
		grade = "B"
  	elif score in range (70, 79):
	 	grade = "C"
  	elif score in range (0, 69):
		grade = "D"

	print ("Score: {}: Your grade is {}").format(score, grade)

print "End of program"
