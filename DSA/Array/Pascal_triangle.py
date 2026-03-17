def nCr(n, r):
    result = 1
    for i in range(r):
        result*=(n-i)/(i+1)
    return result


def printPascalTriangle(n):
    outerList = []
    for i in range(n + 1):
        innerList = []
        elem = 1
        for j in range(i + 1):
            innerList.append(elem)
            elem = elem * (i - j) // (j + 1)
        outerList.append(innerList)
    return (outerList)

print(printPascalTriangle(6))