arr = [1,1,2,2,3,3,4,4,5,6,6,7,7,8,8,9,9]

def numNotTwice(arr):
    n = ((len(arr)//2) + 1)
    oSum = (n*(n+1)/2)
    lSum = 0
    for i in range(len(arr)):
        lSum += arr[i]
    return 2*oSum - lSum

print(numNotTwice(arr))
