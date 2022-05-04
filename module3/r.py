# Test_list = [[4, 5, 6, 8],
#               [1, 2, 3, 1],
#               [7, 8, 9, 4],
#               [1, 8, 7, 5]]
# Result = []
# for i in range(len(Test_list)):
 
#         # If the elements if First or Last then print it as it is...
#     if i == 0:
#         Result.append(Test_list[i])
#         Result = Result[0]
#         print(*Result)
#         Result = []

a = [1,2,3,4,5,6,7]
for i in range(len(a)-1,-1,-1):
    print(i)