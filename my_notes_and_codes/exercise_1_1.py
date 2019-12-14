		
def is_prime(number):
	'''
	Receive a number and outputs whether or not the number is prime or not
	'''
	while (True):
				#request an input from the user and check if it is valid
		try:
			number = int(number)
			break
		except ValueError:
			print("That was no valid number.  Try again...")
			number = input("Please enter a number: ")
	if number > 1:
		# If the number is smaller than one it can't be prime
		for i in range(2, number//2):
			#iterate over the possible values that would contradict the chance of being prime
			if (number % i) == 0:
				print("{} is not a prime number".format(number))
				prime = True
				break
				
		else:
			print("{} is a prime number".format(number))
			prime = True
	else:
		print("{} is not a prime number".format(number))
		prime = True
	return prime