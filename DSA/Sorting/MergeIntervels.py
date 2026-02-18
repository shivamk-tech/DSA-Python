arr = [[8,10], [1,3], [2,6], [3,10], [5,9], [12,10]]
  
def SortBySelection(arr):
    for i in range (len(arr)):
        min_index = i
        for j in range (i+1,len(arr)):
            if(arr[min_index][0] > arr[j][0]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def SortOfIntervel(arr):
    SortBySelection(arr)
    OverLaped = []
    Current = arr[0]
    for i in range(1, len(arr)):
        if(arr[i][0] <= Current[1]):
            Current[1] = max(arr[i][1], Current[1])
        else:
            OverLaped.append(Current)
            Current = arr[i]
    OverLaped.append(Current)
    return OverLaped

print(SortOfIntervel(arr))