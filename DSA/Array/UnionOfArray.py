arr1 = [2,3,3,5,6,7,8,9]
arr2 = [4,4,6,8,8,9,10,11,12]

def unionOfArray(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j] :
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j+=1
        else:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i+=1

    while j < len(arr2):
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j+=1
    while i < len(arr1):
        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i+=1
    return result

print(unionOfArray(arr1, arr2))