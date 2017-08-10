import random
random_num = random.random()

x = .23945593
y = .798839238

x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1


def coin_toss():
	number_head = 0
	number_tail = 0
	for number in range (1, 2000):
		random_num = round(random.random())
		if random_num == 1:
			random_num = "head"
			number_head += 1
		if random_num == 0:
			random_num = "tail"
			number_tail += 1

		print 'Attempt #' + str(number) + " Throwing a coin... It's a " + str(random_num) + '! Got ' + str(number_head) + ' head(s) so far and ' + str(number_tail) + ' tail(s) so far'
coin_toss()