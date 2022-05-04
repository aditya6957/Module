'''
A program to check Palindrome
'''
def palindrome(string):
    '''
    Defined function to check Palindrome
    '''
    #pointers
    for_point = 0
    back_point = len(string)-1
    while for_point < back_point:
        if string[for_point] != string[back_point]:
            return False
        for_point = for_point + 1
        back_point = back_point -1
    return True

if __name__ == "__main__":
    your_string = input("Enter your string: ")
    print(palindrome(your_string))
