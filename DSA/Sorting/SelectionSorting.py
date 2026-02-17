arr = [56,24,57,98,13,56,87]

def SortingArray(arr):
   
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1 , len(arr)):
            if(arr[min_index] > arr[j]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
                
    return arr
       
print(SortingArray(arr))