import sys
import math


def InputSudoku(su):
    print('Enter matrix Sudoku: ')
    for i in range(9):
        x = list(map(int,sys.stdin.readline().strip().split()))
        su.append(x)

def PrintSudoku(su):
    for i in range(9):
        for j in range(9):
            if (j + 1) % 3 == 0 and j != 8:
                print(su[i][j],end = ' | ')
            else:
                print(su[i][j], end = ' ')
        if (i + 1) % 3 ==0 and i != 8:
            print('\n-----------------------')
        else:
            print('')

def Check(su,row,col,k):
    for i in range(9):
        if su[row][i] == k:
            return False
    for i in range(9):
        if su[i][col] == k:
            return False
    a,b = row//3, col//3
    for i in range(3*a,3*a+3): 
        for j in range(3*b,3*b+3):
            if su[i][j] == k:
                return False
    return True

def Solve_Sudoku(su,row,col):
    #print('y = ',row, 'x = ',col,'su[x,y]=' ,su[row][col])
    if col == 9 and row == 8:
        return True
    if col == 9:
        return Solve_Sudoku(su, row + 1, 0)
    if su[row][col] > 0:
        return Solve_Sudoku(su, row, col+1)
    for i in range(1,10):
        if Check(su, row, col, i) == True:
            su[row][col] = i
            if Solve_Sudoku(su, row, col+1) == True:
                return True
            su[row][col] = 0
    return False

# su = []
# InputSudoku(su)
# if Solve_Sudoku(su, 0, 0):
#     PrintSudoku(su)
# else:
#     print('-1')


# k = int(input("Enter a number: "))
# try:
#     s = math.sqrt(k)
#     print("The sqrt of ",k," is ", s)

# except :
#     print("Can not take sqrt of negative number")



