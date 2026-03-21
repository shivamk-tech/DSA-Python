arr = [2,5,7,7,4,7,9,5,4]

def optimalSol(nums, k):
    prefixXor = {0:1}
    count = 0
    xor = 0
    for i in range(len(nums)):
        xor^=nums[i]
        rem = xor^k
        if rem in prefixXor:
            count+=prefixXor[rem]
        prefixXor[xor] = prefixXor.get(xor, 0) + 1
    return count

print(optimalSol(arr, 3))