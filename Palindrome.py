def remove(string):
    string.replace(" ","")

x = input("input to check for palindrome:\n")
remove(x)
y = list(x)

if y == y[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


