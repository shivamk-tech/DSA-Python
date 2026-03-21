arr = [1,2,-1,-2,2,0,-1]

def fourSum(nums, target):
    hashMap = {}
    result = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                rem = target -(nums[i] + nums[j] + nums[k])
                if (i != j and j != k and k != i):
                    if rem in hashMap:
                        if(hashMap[rem] != i and hashMap[rem] != j and hashMap[rem] != k):
                            result.append(tuple(sorted([nums[i] , nums[j] , nums[k], rem])))
                    hashMap[nums[k]] = k
    return list(set(result))

def optimalSol(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            tempTarget = target - (nums[i] + nums[j])
            low = j + 1
            high = len(nums) - 1
            while(low < high):
                if(nums[low] + nums[high] == tempTarget):
                    result.append([nums[low], nums[high], nums[i] , nums[j]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low+=1
                    high-=1
                elif(nums[low] + nums[high] > tempTarget):
                    high-=1
                else:
                    low+=1
    return result


print(optimalSol(arr,0))

