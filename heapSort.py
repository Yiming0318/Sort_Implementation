"""
This is a heap sort implmentation (binary tree)
Time Complexity:O(nlog(n))
Space Complexity: O(1)
"""
def parent(index):
    """
    Method -- parent:
        get the parent index of current index
    Parameter:
        index -- current index
    Return:
        parent index
    """
    return (index - 1) // 2

def left_child(index):
    """
    Method -- left_child:
        get the left child index of current index
    Parameter:
        index -- current index
    Return:
        left child index
    """
    return index * 2 + 1

def right_child(index):
    """
    Method -- right_child:
        get the left child index of current index
    Parameter:
        index -- current index
    Return:
        right child index
    """
    return index * 2 + 2

def heap_sort(array):
    """
    Method -- heap_sort:
        use heap data structure to sort the array
    Parameter:
        array -- array given to sort
    Return:
        None, sort in place
    """
    make_max_heap(array)
    for i in range(len(array), 0, -1):
        delete_max(array, i)

def make_max_heap(array):
    """
    Method -- make_max_heap:
        make an array to a max heap binary tree data structure
    Parameter:
        array -- array given to make max heap
    Return:
        None, transfer to max heap in place
    """
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i)

def heapify(array, n, i):
    """
    Method -- heapify:
        make an array to a max heap binary tree data structure
    Parameter:
        array -- array given to make max heap
        n -- the length of array - 1
        i -- current start parent index for the heap tree 
    Return:
        None, transfer to max heap in place
    """
    largest_value_index = i
    if left_child(i) < n and array[left_child(i)] > array[largest_value_index]:
        largest_value_index = left_child(i)
    if right_child(i) < n and array[right_child(i)] > array[largest_value_index]:
        largest_value_index = right_child(i)
    if largest_value_index == i:
        return
    # swap
    array[largest_value_index], array[i] = array[i], array[largest_value_index]
    # recursion, keep heapify next subtree
    heapify(array, n, largest_value_index)

def delete_max(array,n):
    """
    Method -- heapify:
        delete the max value in max heap
    Parameter:
        array -- array given to delete max value
        n -- the length of array
    Return:
        None, max value will be putted at the end of array
    """
    array[0], array[n-1] = array[n-1], array[0]
    n = n - 1
    heapify(array, n, 0)

array1 = [5,4,3,2,1]
array2 = [3,3,2,6,5]
array3 =[]
heap_sort(array1)
heap_sort(array2)
heap_sort(array3)
print(array1)
print(array2)
print(array3)
