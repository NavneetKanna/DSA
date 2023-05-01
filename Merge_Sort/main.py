# Time Complexity = O(no of comparisons per step * no of steps) = O(nlogn)
# Space Complexity = O(n)


def divide(arr):
    print(f"----------")
    print(f"arr {arr}")
    if len(arr) <= 1:
        print(f"len of arr <= 1 {arr}")
        return arr 
    else:
        print(f"len {len(arr)}")
        mid = (len(arr) - 1 )// 2
        print(f"mid {mid}")
        left_half = divide(arr[:mid])
        right_half = divide(arr[mid:])

        return merge(left_half, right_half)
    
def merge(left, right):
    print("merge")
    print(f"left {left}")
    print(f"right {right}")

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
    print(f" len {len(test_arr)}")
    ans = divide(test_arr)
    print(ans)



