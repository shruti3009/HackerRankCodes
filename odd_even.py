def odd_even(num):
	'''
	this function catergorizes the given number \
	under weird not weird categories on the basis \
	of divisibility
	Input: int
	Return: None
	'''
	if num % 2 != 0:
		print "Weird"
	elif num in range(2,6) and num % 2 == 0:
		print "Not Weird"
	elif num in range(6, 21) and num % 2 == 0:
		print "Weird"
	elif num > 20 and num % 2 == 0:
		print "Weird"
