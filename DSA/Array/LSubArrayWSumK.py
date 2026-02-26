arr =[ 1,2,3,3,4,5,6,6,7,7,8,9]

def LongSubArrayWithSumK(arr, k):
    SumKList = []
    for i in range(len(arr)):
        Sum = 0
        for j in range(i, len(arr)):
            Sum += arr[j]
            if(Sum == k and (j-i+1) > len(SumKList)):
                SumKList = arr[i:j+1]
    return len(SumKList)

def LongSubArrayWith2pointer(nums, k):
    sum = nums[0]
    left = 0
    right = 0
    maxLen = 0
    n = len(nums)
    while(right < n):
        while(left <= right and sum > k):
            sum-=nums[left]
            left+=1
        if(sum == k ): 
            maxLen =max (maxLen, right - left + 1) 
        right+=1
        if(right < n):
            sum+=nums[right]
    return maxLen



print(LongSubArrayWith2pointer(arr, 13))


            
            


