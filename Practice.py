arr = [2, 7, 11, 15]

def Practice(nums, target):
   hashDict = {}
   for i in range(len(nums)):
      needed = target - nums[i]
      if needed in hashDict:
         return [hashDict[needed], i]
      hashDict[nums[i]] = i
   return -1

print(Practice(arr,17))