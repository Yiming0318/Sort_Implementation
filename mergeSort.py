"""
This is a merge sort implmentation
Time Complexity:O(nlog(n))
Space Complexity: O(n)
"""
def merge_sort(nums):
    """
    Method -- merge_sort:
        use divide and conquer to sort the array
    Parameter:
        nums -- nums array
    Return:
        sorted array
    """
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = nums[:middle]
    right = nums[middle:]
    return combine_merge(merge_sort(left), merge_sort(right))


def combine_merge(num1, num2):
    """
    Method -- combine_merge:
        combine num1 and num2 sorted into num3
    Parameter:
        num1 -- nums array 1
        num2 -- nums array 2
    Return:
        merged num3
    """
    num3 = [None] * (len(num1) + len(num2))
    i = 0
    j = 0
    k = 0
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            num3[k] = num1[i]
            i += 1
        else:
            num3[k] = num2[j]
            j += 1
        k += 1
    
    while i < len(num1):
        num3[k] = num1[i]
        i += 1
        k += 1
    
    while j < len(num2):
        num3[k] = num2[j]
        j += 1
        k += 1
    return num3

array1 = [1,2,3,4,5]
array2 = [2,3,4,5,2,3,4]
array3 = []

a1 = merge_sort(array1)
a2 = merge_sort(array2)
a3 = merge_sort(array3)

print(a1)
print(a2)
print(a3)