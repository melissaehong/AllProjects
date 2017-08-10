#print odds from 1 to 1000
def odd_print():
  for odds in range (1, 1000):
    if odds % 2 == 1:
      print odds
debug(odd_print())

# for index in range (1, 1000, 2):
#    print index
#or
# if index % 2 != 0:
#    print index

# odd_print()


#prints multiples of 5 from 5 to 1,000,000
def multiple_5():
  for multiples in range (5, 1000005):
  	if multiples % 5 == 0:
  		print multiples

#multiple_5()