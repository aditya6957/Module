from re import search

def BubbleSort(test_list):
    flag = 0
    i = 1
    for i in range(1, len(test_list)):
        if(test_list[i] < test_list[i - 1]):
            flag = 1
        i += 1
    
    if(not flag):
        print("The list is already sorted")
    else:
        for i in range(len(test_list)-1,0,-1):
            for j in range(i):
                if test_list[j]>test_list[j+1]:
                    temp = test_list[j]
                    test_list[j] = test_list[j+1]
                    test_list[j+1] = temp
        print(test_list)
	

x = int(input("Enter the size of your list: "))
test_list = []
for i in range(0,x):
    print("Enter element number: ", i+1)
    elements = int(input())
    test_list.append(elements)
print("Your list is: \n", test_list)
print("\n")
print("Your sorted list is: \n")
print(BubbleSort(test_list))