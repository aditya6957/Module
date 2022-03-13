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
        print("Your sorted list is: ")
        print(test_list)
	
test_data = list(input("enter your elements sepetrated by space: ").strip().split())
BubbleSort(test_data)
