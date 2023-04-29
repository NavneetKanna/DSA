# Time Complexity = (n-1) iterations x (n-1) comparisons = O(n2)
# For each iteration we are doing comparisons
# Space Complexity = since no additional memory is used = O(1) 

def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        n = n - 1
    
    print(arr)


inp = [7, 4, 9, 1, 5]

bubble_sort(inp)