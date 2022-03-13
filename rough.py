from re import search

def BubbleSort(test_list):
    iterations = 0
    for i in range(len(test_list)-1):
        is_sorted = True
        iterations += 1
        for j in range(len(test_list)-1):
            if test_list[j] > test_list[j+1]:
                # swapping
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
                is_sorted = False

        if is_sorted:
            break
    print(f"iterations done: {iterations}")
    return True


if __name__ == "__main__":
    # x = int(input("Enter the size of your list: "))
    test_data = [
        [2, 1, 5, 3]
    ]

    for test_array in test_data:
        print("\n {}".format("-"*50))
        print("orig list is: \n", test_array)
        ret = BubbleSort(test_array)
        print("sorted list is: \n", test_array)