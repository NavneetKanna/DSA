# arr = sorted array
# Time complexity = O(logn)


def binary_search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return "Does not exist" 


if __name__ == '__main__':
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))