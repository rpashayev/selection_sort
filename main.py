def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr1 = [3, 4, 2, 1]
arr2 = [8, 6, 2, 3, 1, 4, 7, 9, 0, 5]
print(selection_sort(arr1))
print(selection_sort(arr2))
