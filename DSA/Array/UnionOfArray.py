arr1 = [2,3,3,5,6,7,8,9]
arr2 = [4,4,6,8,3,8,5,7,8,4,2]

def unionOfArray(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if(arr1[i] != arr2[j]):
                arr1.append(arr2[j])
    return arr1

print(unionOfArray(arr1, arr2))