'''
A program to sort and eliminate repeted items from list
'''
def unique_sort(test_list):
    '''
    A function to sort and eliminate repeted items from list
    '''
    is_sorted = True
    i = 0
    for i in range(1, len(test_list)):
        if test_list[i] < test_list[i - 1]:
            is_sorted = False
    if is_sorted:
        sorted_list = test_list
        print("The list is already sorted")
    else:
        for i in range(len(test_list)-1):
            for j in range(len(test_list)-1):
                if test_list[j]>test_list[j+1]:
                    test_list[j],test_list[j+1]=test_list[j+1],test_list[j]
        sorted_list = test_list
        for i in range(len(sorted_list)):
            # Move the index ahead while there are duplicates
            if(i < (len(sorted_list)-1) and sorted_list[i] == sorted_list[i+1]):
                i+=1
            # print last occurrence of the current element
            else:
                print(sorted_list[i], end=" ")

if __name__ == "__main__":
    your_list = list(input("Enter your items seperated by comma: ").split(','))
    unique_sort(your_list)
