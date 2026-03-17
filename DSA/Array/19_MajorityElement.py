arr = [1,1,1,2,2,2,2,3,3,3]

# brute force

def bruteForce(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        num = nums[i]
        for j in range(i, len(nums)):
            if(nums[j] == num):
                count+=1
        if(count > (len(nums)//3)):
            result.append(nums[i])
    return list(set(result))


def optimaalSolution(nums):
    count1 = 0
    count2 = 0
    el1 = None
    el2 = None
    for i in range(len(nums)):
        if nums[i] == el1:
            count1 += 1
        elif nums[i] == el2:
            count2 += 1
        elif count1 == 0:
            el1 = nums[i]
            count1 = 1
        elif count2 == 0:
            el2 = nums[i]
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    result = []
    count1 = nums.count(el1)
    count2 = nums.count(el2)

    if count1 > len(nums) // 3:
        result.append(el1)
    if (count2 != count1 and count2 > len(nums) // 3):
        result.append(el2)
    return result

print(optimaalSolution(arr))