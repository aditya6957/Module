'''
Program to print G patterns from stars
'''
def g_pattern(lines):
    '''
    Functions to print G
    '''
    # rows
    if lines%2 == 1:
        lines = lines-1
    for row in range(lines):
        # columns
        for col in range(lines):
            if ((row == 0 and (col != 0 and col != lines-1)) or
                (row == lines - 1 and (col != 0 and col != lines-1)) or
                ((col == 0 and (row != 0 and row != lines-1)) or
                 (col == lines-1 and row != lines-1 and row >= (lines/2)-1)) or
                (row == (lines/2)-1 and ((lines/2)-1 <= col < lines-1))
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    pattern_lines = int(input("Enter the size you want:\t"))
    g_pattern(pattern_lines)
