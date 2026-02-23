arr1 = [2,3,3,5,6,7,8,9]
arr2 = [4,4,6,8,8,9,10,11,12]

def interSectionArray(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) - 1 and j < len(arr2) - 1:
        if arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    return result

print(interSectionArray(arr1, arr2))