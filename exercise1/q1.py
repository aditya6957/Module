data = """first line 
second line 
third line
fourth line
fifth line"""

split_data = data.split("\n")
initial = []
list1 = []
list2 = []
for i in split_data:
    final = i.strip()
    initial.append(final)


count = 1
#for i in range(2):
while count < len(initial):
    list1 = []
    list1.append(initial[0])
    for i in range(2):
        list1.append(initial[count])
        count += 1
    list2.append(list1)
    #list1.append(split_data[count + 1])
print(initial)
print(list1)
print(list2)
# initial.append(split_data[0])
# print(initial)

# for i in split_data:
#     print(i)

# list1 = split_data[1]
# print(list1)
