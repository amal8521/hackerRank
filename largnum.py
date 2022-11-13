arr = [3,0,5,4,7]
n = len(arr)
max = 0
for i in range(0, n):
    if(arr[i] > max):
        max = arr[i]
print(max, "is the largest element")


