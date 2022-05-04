'''
program to generate dictionary and search key value with index
'''
def dict_generator():
    '''
    Function to generate dictionary
    '''
    resulting_dict = {}
    dict_len = int(input("Enter the length of your dictionary: "))
    for i in range(dict_len):
        print("Enter your key and values for index: ",i)
        key = input("Enter the key: ")
        value = input("Enter the corrosponding value: ")
        resulting_dict.update({key:value})
    return resulting_dict

def search_key(your_dict, var_key):
    '''
    function to search key value with index
    '''
    if var_key in your_dict:
        return print("Your key value exists in the created dictionary at the index: "
        ,[i for i, t in enumerate(your_dict) if t[0]== var_key])
    else:
        return print("Your key does not exists")

if __name__ == "__main__":
    your_dict = dict_generator()
    print(your_dict)
    #var_key = input(print("Enter the key value you want to search: "))
    search_key(your_dict, input("Enter the key value you want to search: "))
