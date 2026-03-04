arr =[1,2,3,3,4,5,6,6,7,7,8,9]

def Practice(nums,k):
    SumKlist = []
    for i in range(len(nums)):
        Sum = 0
        for j in range(i, len(nums)):
            Sum += nums[j]
            if Sum == k and (j-i+1) > len(SumKlist):
                SumKlist = nums[i:j+1]
    return len(SumKlist)

print(Practice(arr, 13))