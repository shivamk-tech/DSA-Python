str = "madam"

def RevAnArr(arr,start,end):
    if(start > end):
        print("String is palindrome")
        return
    if(str[start] != str[end]):
        print("It is not an palindrome")
        return
    start+=1
    end-=1
    RevAnArr(arr,start,end)

start = 0
end = len(str) - 1

RevAnArr(str,start,end)


