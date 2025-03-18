def two_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum < target: 
            left += 1  
        else:
            right -= 1 
    return False
arr = [4,5,11,8,21,7,3]
target = 9
if two_sum(arr, target):
    print("true")
else:
    print("false")
