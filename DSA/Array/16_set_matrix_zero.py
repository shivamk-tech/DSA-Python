matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Brute Force Solution
def markRowZero(i):
    for j in range(len(matrix[0])):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1

def markColZero(j):
    for i in range(len(matrix)):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1

def setMatrixZero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                markRowZero(i)
                markColZero(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == -1):
                matrix[i][j] = 0
    return matrix
    
# Better Solution

def betterSol(matrix):
    rowDict = {}
    colDict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                rowDict[i] = 1
                colDict[j] = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(rowDict.get(i) == 1 or colDict.get(j) == 1):
                matrix[i][j] = 0
    return matrix

def optimalSolution(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row0 = 1

    for j in range(n):
            if matrix[0][j] == 0:
                row0 = 0

    for i in range(m):
        for j in range(1,n):
            if(matrix[i][j] == 0):
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1,m):
        for j in range(1,n):
            if(matrix[0][j] == 0 or matrix[i][0] == 0):
                matrix[i][j] = 0

    if(matrix[0][0] == 0):
        for i in range(m):
            matrix[i][0] = 0

    if(row0 == 0):
        for j in range(n):
            matrix[0][j] = 0
            
    return matrix

        

print(optimalSolution(matrix))
