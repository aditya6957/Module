'''
Python program to add even number at odd indices.
'''
def adder():
    '''
    function to create a list and add even numbers at odd indicies.
    '''
    try:
        user_list = []
        while True:
            user_list.append(int(input("Enter the elemetns.\nEnter non integer value to stop: ")))
    except:
        print("Your list is: ", user_list)

    empty_list=[]
    for i in range(len(user_list)):
        if i%2 == 1 and user_list[i]%2==0:
            empty_list.append(user_list[i])
    print(empty_list)
    print(sum(empty_list))

if __name__ == "__main__":
    adder()
