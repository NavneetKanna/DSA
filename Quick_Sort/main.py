
def quicksort(arr, l, r):
    if l < r:
        piviot = partition(arr, l, r)
        quicksort(arr, l, piviot - 1)
        quicksort(arr, piviot + 1, r)

def partition(arr, l , r):
    piviot = r
    i = l - 1

    for j in range(l, r):
        if arr[j] < arr[piviot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[piviot] = arr[piviot], arr[i+1]   

    return i + 1

if __name__ == '__main__':
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    quicksort(test_arr, 0, len(test_arr) - 1)
    print(test_arr)

