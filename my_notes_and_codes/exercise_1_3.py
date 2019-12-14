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


