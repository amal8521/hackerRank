arr = [3,9,123,6,6]
n = len(arr)
max =0
smax = 0
for i in range(n):
    if (max < arr[i]):
        max = arr[i]
for i in range(n):
    if arr[i] == max:
        i += 1
    elif arr[i] > smax:
        smax = arr[i]
print(smax)
