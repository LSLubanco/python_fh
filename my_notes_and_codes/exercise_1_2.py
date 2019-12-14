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
