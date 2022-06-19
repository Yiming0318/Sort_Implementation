"""
This is a counting sort implmentation
Time Complexity:O(n+k)
Space Complexity: O(k)
n is the number of elements and k is the range of elements
"""
def counting_sort(array):
    """
    Method -- counting_sort:
        use a k size help array to sort the array
    Parameter:
        nums -- nums array
    Return:
        sorted array
    """
    if not array: return []
    n = len(array)
    range_of_elements = max(array) + 1
    # initialize the final array and help array
    sorted_array = [0] * n
    help_array = [0] * range_of_elements
    # count the frequency of each number in original array
    for i in range(n):
        help_array[array[i]] += 1
    # calculate the prefix for the help array
    for i in range(1, len(help_array)):
        help_array[i] += help_array[i-1]
    # put the number into final array based on frequency
    for i in range(n-1,-1,-1): #stable
        number = array[i]
        sorted_array[help_array[number]-1] = number
        help_array[number] -= 1
    return sorted_array


array1 = [0,1,2,3,4,5,5,4,3,2]
sorted_array1 = counting_sort(array1)
print(sorted_array1)


array2 = [4,5,5,4,4,3,2,10,70]
sorted_array2 = counting_sort(array2)
print(sorted_array2)

array3 = []
sorted_array3 = counting_sort(array3)
print(sorted_array3)