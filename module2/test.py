'''
MATRIX
'''
def matrix_maker():
    print("Enter order of your matrix:",)

    # take integer inputs in one line
    m,n = list(map(int,input().split()))

    print("Enter Row wise values")

    # empty list for 1st matrix
    mat1 = []

    # row wise insertion in the matrix
    for i in range(m):
        print("Enter row",i+1,"value:")

        # take 1d- integer array input in one line
        row = list(map(int,input().split()))
        mat1.append(row)
    print("Matrix 1:",mat1)

def matrix_multipier(mat1, mat2):
    
    if len(mat1[0]) != len(mat2):
        print("multiplication not possible")
        exit(1)

    # empty list for resulatant matrix
    resultant = []

    # create a 0-matrix of order m x q
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            row.append(0)

        resultant.append(row)

    print("Matrix Multiplication: ")

    # perform matrix multiplication
    # using nested for loops
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                resultant[i][j] += mat1[i][k] * mat2[k][j]

    # matrix printing row wise
    for row in resultant:
        print(row)

matrix1 = matrix_maker()
matrix2 = matrix_maker()
matrix_multipier(matrix1, matrix2)
       