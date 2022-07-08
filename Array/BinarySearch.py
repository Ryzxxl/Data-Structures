def binarysearch(arr, i, j, x):
    if i == j:
        if arr[i] == x:
            return i
        else:
            return -1

    else:
        mid = i + ( j -i )//2

        if arr[mid] == x:
            return mid

        elif arr[mid] <  x:
            return binarysearch(arr, mid+1, j , x)
        else:
            return binarysearch(arr, mid-1, i , x)

            
arr = [2, 6, 7, 9, 12, 17, 30]
i = 0
j = len(arr) -1
x = 12
result = binarysearch(arr, i, j, x)
print("searching value is present in" , result)