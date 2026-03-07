arr = [2,2,1,1,1,2,2,1,1,2,2]

def MajorityElement(nums):
    hashMap = {}
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
    for key,value in hashMap.items():
        if value > len(nums)/2: return key


# Moore's voting Algorithm

def MajorityByMoores(nums):
    count = 0
    majEl = None
    for i in range(len(nums)):
        if(count == 0):
            majEl = nums[i]
            count +=1
        elif(nums[i] == majEl):
            count+=1
        else:
            count-=1
    return majEl


print(MajorityByMoores(arr))


