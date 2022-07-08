def linearsearch(arr, length,search_element):
    for i in range (length):
        if search_element == arr[i]:
            return arr[i]
        
    return -1

arr = [34, 55, 66, 87, 53, 42, 23]
search_element = 555
length = len(arr)
result = linearsearch(arr, length, search_element)

print('The searched element index is : ', result)