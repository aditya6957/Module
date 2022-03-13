from os import dup


test_list = input("Enter your items seperated by comma: ").split(',')

def Sorting(test_list):
    A = a = 1
    B = b = 2
    C = c = 3
    D = d = 4
    E = e = 5
    F = f = 6
    G = g = 7
    H = h = 8
    I = i = 9
    J = j = 10
    K = k = 11
    L = l = 12
    M = m = 13
    N = n = 14
    O = o = 15
    P = p = 16
    Q = q = 17
    R = r = 18
    S = s = 19
    T = t = 20
    U = u = 21
    V = v = 22
    W = w = 23
    X = x = 24
    Y = y = 25
    Z = z = 26

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

def Unique(test_list):
    UniqueList = []
    for i in test_list:
        if i not in UniqueList:
            UniqueList.append(i)
    return UniqueList

Sorting(Unique(test_list))


