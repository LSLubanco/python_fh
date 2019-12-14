		
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
	
def is_palindrome(text):
#Function to check if an input is a palindorme or not
	text_alpha = ''.join(filter(str.isalpha, text)) # Removing non alphabet characters
	text_alpha = text_alpha.lower()
	text_rev = text_alpha[::-1] #create a temp variable to store the reversed order of the string
	if(text_alpha == text_rev):
		print("{} is a palindrome".format(text))
		return True
	else:
		print("{} is not a palindrome".format(text))
		return False

def scalar(v1,v2):
	'''Given two vectors in a list type, this function calculated the scalar output '''
	while(True):
		if(len(v1)==len(v2)):
			#If lists have the same length we can calculate scalar
			break
		else:
			print("Please make sure that the vectors have the same length")
			v1 = (input("write your first vector(space separated)"))
			v1=[int(i) for i in v1.split()]
			v2 = (input("write your second vector(space separated)"))
			v2=[int(i) for i in v2.split()]
	scalar_val = 0.0
	for k in range(0,len(v1)):
		#Iterate over each element multiply them and add to total sum
		scalar_val += v1[k]*v2[k]

	print("The scalar output is equal to: {}".format(scalar_val))
	return scalar_val
