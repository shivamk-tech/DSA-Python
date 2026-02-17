arr1 = [1,2,4,6,8]
arr2 = [1,4,5,8,9,10,45]

def Merge(arr1, arr2, high1, high2):
    temp = []
    left1 = 0
    left2 = 0
    while (left1 <= high1 and left2 <= high2):
        if(arr1[left1] <= arr2[left2]):
            temp.append(arr1[left1])
            left1+=1
        else:
            temp.append(arr2[left2])
            left2+=1
    while (left1 <= high1):
        temp.append(arr1[left1])
        left1+=1
    while (left2 <= high2):
        temp.append(arr2[left2])
        left2+=1
       
    return temp

low1 = 0
low2 = 0
high1 = len(arr1) - 1
high2 = len(arr2) - 1

print(Merge(arr1, arr2, low1, low2, high1, high2))