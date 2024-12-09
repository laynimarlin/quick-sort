def quick_sort(arr):
    if len(arr) <= 1:  
        return arr
    else:
        pivot = arr[len(arr) // 2] 
        left = [x for x in arr if x < pivot]  
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot]  
        return quick_sort(left) + middle + quick_sort(right)

data = [5, 1, 3, 7, 9, 8, 10]
print("Data sebelum diurutkan:", data)
sorted_data = quick_sort(data)
print("Data setelah diurutkan dengan Quick Sort:", sorted_data)
