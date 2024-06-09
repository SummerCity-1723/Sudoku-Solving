'''
9*9_sudoku solving code made by SC1723(Python版)
Inspired by:BV1DD4y1h7Zg
'''
#input sudoku

sudoku = [[3,6,1,0,0,4,0,0,0],
          [0,0,0,3,0,0,0,0,6],
          [0,7,0,0,0,0,0,0,9],

          [0,0,2,0,1,0,0,5,0],
          [0,0,9,0,0,0,6,0,0],
          [0,5,0,0,2,0,8,0,0],

          [6,0,0,0,0,0,0,1,0],
          [8,0,0,0,0,7,0,0,0],
          [0,0,0,9,0,0,5,6,4]]

def check(row,col):
    global sudoku
    #row check
    check_list=[]
    for i in range(9):
        if sudoku[row][i] in check_list: return 0
        else:
            if sudoku[row][i] != 0:
                check_list.append(sudoku[row][i])
    #col check
    check_list = []
    for j in range(9):
        if sudoku[j][col] in check_list: return 0
        else:
            if sudoku[j][col] != 0:
                check_list.append(sudoku[j][col])
    #3*3 grid check
    check_list = []
    for i in range(row//3*3,row//3*3+3):
        for j in range(col//3*3,col//3*3+3):
            if sudoku[i][j] in check_list: return 0
            else:
                if sudoku[i][j] != 0:
                    check_list.append(sudoku[i][j])
    return 1

def dfs(x,y):
    global sudoku
    if x == 9:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end="")
                if j%3 == 2 and j != 8:
                    print(" | ",end="")
                else:
                    print(" ",end="")
            if i%3 == 2 and i != 8:
                print()
                print("—————————————————————",end="")

            print()
        exit(0)

    curx = x
    cury = y+1
    if cury == 9:
        cury = 0
        curx += 1
    if sudoku[x][y] == 0:#如果数字为0，即可填入
        for i in range(1,10):
            sudoku[x][y] = i
            if check(x,y): dfs(curx,cury)
            sudoku[x][y] = 0
    else: dfs(curx,cury)

#Main Program
dfs(0,0)
#如果没有答案，输出下面这行
print("No Answers!")