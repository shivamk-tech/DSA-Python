arr = [1,2,3,1]

def hashAlgo(nums):
    hashMap = {}
    for i in range(len(nums)):
        hashMap[nums[i]] = hashMap.get(nums[i],0) + 1
    if any(value >= 2 for value in hashMap.values()):
        return True
    else:
        return False

print(hashAlgo(arr))