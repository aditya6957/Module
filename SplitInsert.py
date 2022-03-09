def convertTuple(tup):
    str = ''.join(tup)
    return str
x = "abcd"
x = (x)
c = "AshokaTano"
# y = x.split()
print(x)
z = int((len(x)))
if z%2==0:
    q = int(z/2)
    a = x[0:q]
    b = x[q:z]
    #d = [a,c,b]
    d = (a,c,b)
    e = convertTuple(d)
    print(e)
    e.replace(" ","")
    print(e)
else:
    print("Can not divide the given string")
    