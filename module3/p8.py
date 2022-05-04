def gcd(num_a,num_b):

    if num_a < 0 and num_b > 0:
        return False

    elif num_a > 0 and num_b < 0:
        return False

    else:

        if num_a < 0 and num_b <0:
            num_a = num_a*-1    
            num_b = num_b*-1

        if num_a == 0:
            return num_b

        if num_b == 0:
            return num_a

        if num_a == num_b:
            return num_a

        if num_a > num_b:
            return(gcd(num_a-num_b,num_b))
        
        return(gcd(num_a,num_b-num_a))

def lcm(num1,num2):
    if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
        return (num1 / gcd(num1,num2))* num2
    
    else:
        print("LCM not possible")

if __name__ == "__main__":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print(lcm(first_number, second_number))


    