arr =[1,2,3,4,5,6,7,8,10]

def Practice(nums):
   xor1 = 0
   xor2 = 0
   for i in range(1, len(nums) + 2):
      xor1^=i
   for i in range(len(nums)):
      xor2^=nums[i]
   return xor1^xor2
print(Practice(arr))