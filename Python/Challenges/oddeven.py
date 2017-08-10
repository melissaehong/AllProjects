def odd_even():
	for numbers in range (1, 2001):
		if numbers % 2 == 0:
			print "Number is " + str(numbers) + ". This is an even number."
		if numbers % 2 == 1:
			print "Number is " + str(numbers) + ". This is an odd number."
odd_even()