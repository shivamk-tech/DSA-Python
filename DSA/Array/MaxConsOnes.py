arr = [1,1,0,1,1,1,0,1,1,1,1,1,1]

def maxConsOne(arr):
    maxOnes = 0
    count = 0
    for i in range(len(arr)):
        if(arr[i] == 1):
            count+=1
        elif(arr[i] == 0):
            maxOnes = max(maxOnes, count)
            count = 0
    maxOnes = max(maxOnes, count)
    return maxOnes

print(maxConsOne(arr))