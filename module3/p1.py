'''
Program to calculate maximum possible expenditure in a given budged.
'''
def max_expenditure():
    '''
    Function to create two seperate price list and
    find the maximum possible expenditure in a given budged.
    '''
    try:
        keyboards_prices = []
        while True:
            keyboards_prices.append(int(input("Enter the elemetns.\nNon integer value to stop: ")))
    except:
        print("Your list is: ", keyboards_prices)
    # keyboards_prices = [40, 50, 60, 30]

    try:
        drives_prices = []
        while True:
            drives_prices.append(int(input("Enter the elemetns.\nNon integer value to stop: ")))
    except:
        print("Your list is: ", drives_prices)
    #drives_prices = [5, 8, 12]
    empty_list = []
    budget = int(input("Enter budget: "))
    for i in range(len(keyboards_prices)):
        for j in range(len(drives_prices)):
            exp = keyboards_prices[i] + drives_prices[j]
            if exp <= budget:
                empty_list.append(exp)
                empty_list.sort()
    print(empty_list[-1])

if __name__ == "__main__":
    max_expenditure()
