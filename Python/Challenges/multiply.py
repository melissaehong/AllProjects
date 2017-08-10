def multiply(array, value):
	for i in range (len(array)):
		array[i] = array[i] * value
		return array

print multiply([2,3,4],3)
