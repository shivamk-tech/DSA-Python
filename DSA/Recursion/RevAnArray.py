arr = [i*i for i in range(1,6)]

def RevAnArr(arr,start,end):
    if(start > end):
        return
    arr[start], arr[end] = arr[end], arr[start]
    start+=1
    end-=1
    RevAnArr(arr,start,end)

start = 0
end = len(arr) - 1

RevAnArr(arr,start,end)
print(arr)


