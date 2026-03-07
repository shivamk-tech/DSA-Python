arr = [23, 45 ,67 ,89, 13, 56, 85]

# Medium TimeComplexity Method to do this Question
def SecondLargest(arr):
    largest = arr[0]
    for i in range(1, len(arr) - 1):
        if(arr[i] > largest):
            largest = arr[i]
    SLargest =  -1
    for i in range(len(arr)):
        if(arr[i] > SLargest and arr[i] != largest):
            SLargest = arr[i]
    return SLargest

print("Medium Approach",SecondLargest(arr))

# Optimal Approach to do this question

def SecondLargestOptimal(arr):
    largest = arr[0]
    SLargest =  -1
    for i in range(1, len(arr)):
            if(arr[i] > largest):
                SLargest = largest
                largest = arr[i]
            elif(arr[i] < largest and arr[i] > SLargest):
                 SLargest = arr[i] 
    return SLargest

print("Optimal Approach",SecondLargestOptimal(arr))