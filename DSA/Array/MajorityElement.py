arr = [2,2,1,1,1,2,2,1,1,2,2]

def MajorityElement(nums):
    hashMap = {}
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
    for key,value in hashMap.items():
        if value > len(nums)/2: return key

print(MajorityElement(arr))