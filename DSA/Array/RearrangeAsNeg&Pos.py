nums = [3, 1, -2, -5, 2, -4]

def BruteRearrage(nums):
    pos = [] 
    neg = []
    for i in range(len(nums)):
        if(nums[i] > 0):
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    if(len(pos) > len((neg))):
        for i in range(len(neg)):
            nums[i*2] = pos[i]
            nums[i*2+1] = neg[i]
        for i in range(len(neg), len(pos)):
            nums.append(pos[i])
    else:
        for i in range(len(pos)):
            nums[i*2] = pos[i]
            nums[i*2+1] = neg[i]
        for i in range(len(pos), len(neg)):
            nums.append(neg[i])
    return nums            

print(BruteRearrage(nums))

def Rearrange(nums):
    result = [0] * (len(nums) )
    PosP = 0
    NegP = 1
    for i in range(len(nums)):
        if(nums[i] > 0):
            result[PosP] = nums[i]
            PosP+=2
        if(nums[i] < 0):
            result[NegP] = nums[i]
            NegP+=2

    return result

print(Rearrange(nums))
