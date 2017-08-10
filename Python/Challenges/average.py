# create a program that prints avg values of the list:
# a = [1, 2, 5, 10, 255, 3]

def print_avg():
	a = [1, 2, 5, 10, 255, 3]
	sum = a[0] + a[1] + a[2] + a[3] + a[4] + a[5]
	avg = sum/6
	print avg

print_avg()