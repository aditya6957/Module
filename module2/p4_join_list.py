'''
Program to find common elements in two lists
'''
def common_elements(list1, list2):
    '''
    Function to find common elements in two lists
    '''
    result = []
    for element in list1:
        if element in list2 and element not in result:
            result.append(element)
    return result

if __name__ == "__main__":
    list_1 = list(input("Enter your items seperated by comma: ").split(','))
    list_2 = list(input("Enter your items seperated by comma: ").split(','))
    print(common_elements(list_1, list_2))
