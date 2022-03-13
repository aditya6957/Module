from re import search

def BubbleSort(test_list):
    sorted = True
    i = 1
    for i in range(1, len(test_list)):
        if(test_list[i] < test_list[i - 1]):
            sorted = False
    
    if(sorted):
        print("The list is already sorted")
    else:
        for i in range(len(test_list)-1):
            for j in range(len(test_list)-1):
                if test_list[j]>test_list[j+1]:
                    test_list[j],test_list[j+1]=test_list[j+1],test_list[j]
        print("Your sorted list is: ")
        print(test_list)
	
test_data = list(input("enter your elements sepetrated by space: ").strip().split())
BubbleSort(test_data)
