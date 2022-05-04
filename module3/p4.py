'''
Function to print Matrix in Z form
'''
def Z_print(Test_list):

	Result = [] # Empty list to Store Final Result

	# To find the difference b/w whole matrix and first elements
	diff = len(Test_list)-len(Test_list[0])

	# Loop to find elements for Z form and to print it.
	for i in range(len(Test_list)):

		# If the elements if First or Last then print it as it is...
		if i == 0 or i == len(Test_list)-1:
			Result.append(Test_list[i])
			Result = Result[0]
			print(*Result)
			Result = []
		else:
			Result.append(Test_list[i][len(Test_list)-i-1-diff])
			a = Result[0]
			# Give require spaces for printing elements...
			print(" " * (len(Test_list)-i-1-diff) + str(a))
			Result = [] # Empty list again for storing next pattern

	return Result


# Driver Function
if __name__ == "__main__":
	Test_list1 =[[4, 5, 6, 8],
				[1, 2, 3, 1],
				[7, 8, 9, 4],
				[1, 8, 7, 5]]
	Z_print(Test_list1) # Passing Matrix to Z_print function
