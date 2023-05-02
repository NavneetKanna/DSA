# https://www.youtube.com/watch?v=Vtckgz38QHs

# Time Complexity = O(n2)
# Space Complexity = O(logn)

def quicksort(arr, l, r):
    if l < r:
        piviot = partition(arr, l, r)
        quicksort(arr, l, piviot - 1)
        quicksort(arr, piviot + 1, r)

def partition(arr, l , r):
    pivot = r
    i = l - 1

    for j in range(l, r):
        if arr[j] < arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]   

    return i + 1

if __name__ == '__main__':
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    quicksort(test_arr, 0, len(test_arr) - 1)
    print(test_arr)



"""
An alternatice approach, but not suitable for large arrays 

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quicksort(left) + middle + quicksort(right)
"""