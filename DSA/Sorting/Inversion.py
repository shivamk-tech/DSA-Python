arr = [4, 3, 2, 1]
count = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if (i < j and arr[i] > arr[j]):
            count+=1
print(count)
