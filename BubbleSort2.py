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


test_data = list(input("enter your elements sepetrated by space: ").strip().split())
BubbleSort(test_data)
print(test_data)
