# Time Complexity = O(no of comparisons per step * no of steps) = O(nlogn)
# Space Complexity = O(n)

# The reason we dont do len() - 1 is because // returns the floor, so if we 
# subtract 1 we are shiftting the mid by 1 which is not correct 
def divide(arr):
    if len(arr) <= 1:
        return arr 
    else:
        mid = len(arr) // 2
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
    print(f"result {result}")
    return result


if __name__ == '__main__':
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    ans = divide(test_arr)
    print(ans)



