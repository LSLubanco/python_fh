

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--number", type=int, required=False,
	help="define the number that you want to check")
args = vars(ap.parse_args())

number = (args["number"])
#print(number) Debugging
done = False
while(done != True):
	#If number input has not be given, just skip checking
	if number == None:
		pass
	else:
		if number > 1:

		    for i in range(2, number//2):
		        if (number % i) == 0:
		        	print("{} is not a prime number".format(number))
		        	break
		            #break
		    else:
		    	print("{} is a prime number".format(number))

		else:
		   print("{} is not a prime number".format(number))

	while(True):
		value = input("\n Do you want to check another number? [y/n]\n")
		if(value == 'y'):
			while (True):
				#request an input from the user and check if it is valid
				try:
					number = int(input("Please enter a number: "))
					break
				except ValueError:
					print("That was no valid number.  Try again...")
				
			break
		elif(value=='n'):
			done = True
			break
		else:
			print("Invalid input. Try it again.")
			
