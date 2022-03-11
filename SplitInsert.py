# def convertTuple(tup):
#     str = ''.join(tup)
#     return str
# x = "abcd"
# x = (x)
# c = "AshokaTano"
# # y = x.split()
# print(x)
# z = int((len(x)))
# if z%2==0:
#     q = int(z/2)
#     a = x[0:q]
#     b = x[q:z]
#     #d = [a,c,b]
#     d = (a,c,b)
#     e = convertTuple(d)
#     print(e)
#     e.replace(" ","")
#     print(e)
# else:
#     print("Can not divide the given string")
    

def insert_sting_middle(str, word):
    # str = input("Enter your string")
    # word = input("Enter what you want to insert")
    print(str[:len(str)//2]+word+str[len(str)//2:])

yourstring = input("Enter your string: \n")
word = input("Enter what you want to insert: \n")
insert_sting_middle(yourstring, word)
