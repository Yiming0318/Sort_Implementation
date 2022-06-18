"""
This is a quick sort implmentation
Average Time Complexity:O(nlog(n)), Worst O(n^2)
Space Complexity: O(1)
"""
def median_of_three(nums, left, right):
    """
    Method -- median_of_three:
        get the median of a, b ,c
    Parameter:
        a - number 1
        b - number 2
        c - number 3
    Return:
        mid -- the meidian number
    """
    mid = left + (right - left) // 2
    a = nums[left]
    b = nums[mid]
    c = nums[right]
    if a <= b and b <= c:
        return b, mid
    if c <= b and b <= a:
        return b, mid
    if a <= c and c <= b:
        return c, right
    if b <= c and c <= a:
        return c, right
    return a, left




def partition(left, right, nums):
    """
    Method -- partition
        split the array into two part, 
        let left part numbers smaller than pivot
        let right part numbers lager than pivot
    Parameter:
        left -- smallest index for this partition
        right -- largest index for this partition
        nums -- nums array
    Return:
        pivot_index -- the pivot index
    """
    pivot, p_i = median_of_three(nums,left,right)
    # swap the pivot to the right
    nums[p_i], nums[right] = nums[right], nums[p_i]
    l = left - 1
    for r in range(left, right):
        if nums[r] < pivot:
            l += 1
            nums[r], nums[l] = nums[l], nums[r]
    # final swapping
    # swap pivot to l+1 index
    nums[right], nums[l+1] = nums[l+1], nums[right]
    return l+1


def quick_sort(left, right, nums):
    if left <= right:
        pivot = partition(left, right, nums)
        quick_sort(left, pivot-1, nums)
        quick_sort(pivot+1, right, nums)
    

array = [5,2,3,1]
array2 = [2,2,2,4,6,3]
array3 = []
quick_sort(0, len(array)-1, array)
quick_sort(0, len(array2)-1, array2)
quick_sort(0, len(array3)-1, array3)
print(array)
print(array2)
print(array3)