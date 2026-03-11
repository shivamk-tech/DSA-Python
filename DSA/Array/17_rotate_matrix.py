matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Brute Force
def bruteForce(matrix):
    m = len(matrix)
    n = len(matrix[0])
    resultMat = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
           resultMat[j][m-1-i] = matrix[i][j]
    return resultMat

# Better Solution here

def betterSolution(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(m):
        low = 0
        high = n - 1
        while(low < high):
            matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
            low+=1
            high-=1
    return matrix

print(betterSolution(matrix))