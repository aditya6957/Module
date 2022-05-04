def identity_matrix(order):
    for row in range(order):
        for column in range(order):
            if row == column:
                print(1, end = " ")
            else:
                print(0, end = " ")
        print()

if __name__ == "__main__":
    identity_matrix(int(input("Enter order of matrix: ")))