# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# x = []

# for i in range(1,num2+1):
#     for j in range(1, num1+1):
#         if num2*j == num1*i:
#             print(num2*j)
#             x.append(num2*j)
# print(x[0])

# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b
def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 1.5
b = 2.1
print('LCM of', a, 'and', b, 'is', lcm(a, b))

# This code is contributed by Danish Raza

