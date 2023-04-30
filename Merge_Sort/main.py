# Time Complexity = O(no of comparisons per step * no of steps) = O(nlogn)
# Space Complexity = O(n)


def divide(arr):
    if len(arr) <= 1:
        return arr 
    else:
        mid = (len(arr) ) // 2
        left_half = divide(arr[:mid])
        right_half = divide(arr[mid:])

        return merge(left_half, right_half)
    
def merge(left, right):
    i = 0
    j = 0

    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]  # Append remaining elements using slicing
    result += right[j:]  # Append remaining elements using slici

    return result


if __name__ == '__main__':
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    ans = divide(test_arr)
    print(ans)



