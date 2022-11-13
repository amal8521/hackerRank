# Its in ascendin order
arr = [9,3,4,7,1,2]
n = len(arr)
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:        #change if > to < if you want descending order
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)