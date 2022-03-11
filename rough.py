# Python3 code to demonstrate
# to check if list is sorted
# using naive method

# initializing list
test_list = [1, 4, 9, 8, 10]

# printing original list
print ("Original list : " + str(test_list))

# using naive method to
# check sorted list
flag = 0
i = 1
while i < len(test_list):
	if(test_list[i] < test_list[i - 1]):
		flag = 1
	i += 1
	
# printing result
if (not flag) :
	print ("Yes, List is sorted.")
else :
    for i in range(len(test_list)-1,0,-1):
        for j in range(i):
            if test_list[j]>test_list[j+1]:
                temp = test_list[j]
                test_list[j] = test_list[j+1]
                test_list[j+1] = temp
    print(test_list)
