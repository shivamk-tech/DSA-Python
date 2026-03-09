arr = [1,1,0,1,1,1,1,1,0,1,1,1]

def Practice(nums):
   maxLen = 0
   count = 0
   for i in range(len(nums)):
      if(nums[i] == 1):
         count+=1
         maxLen = max(maxLen, count)
      elif(nums[i] == 0):
         count = 0
   return maxLen
   
print(Practice(arr))