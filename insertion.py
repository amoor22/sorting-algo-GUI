arr = [6, 5, 1, 0, 4, 3]

for i in range(1, len(arr)):
    current = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[j] > current:
            arr[j + 1] = arr[j]
            arr[j] = current
print(arr)

