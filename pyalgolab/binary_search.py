#template
# Binary Search
def binary_search(arr, target): #return the position of first number which is bigger or equal to target
    #开区间写法 （）
    left, right = -1, len(arr)
    while left + 1 < right: 
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid 
        else:
            right = mid 
    return right if right < len(arr) else -1

# >  : (>= x + 1)
# <  : (>=x) - 1
# <= : (>x) - 1

