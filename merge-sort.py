
def merge(left_array, right_array):
    # Base cases
    smallest_number = 0
    if (len(right_array) == 0):
        return left_array  # We have nothing to compare. Left wins.
    if (len(left_array) == 0):
        return right_array  # We have nothing to compare. Right wins.

    # Get the lowest value and remove it from the array
    if (left_array[0] <= right_array[0]):
        smallest_number = left_array.pop(0)
    else:
        smallest_number = right_array.pop(0)

    # We keep doing it until the left or right array is empty
    merged = merge(left_array, right_array)
    merged.insert(0, smallest_number)
    # Okay, either left or right array are empty at this point. So we have a result
    return merged


def merge_sort(arr):
    # base case:
    # an array of 1 or fewer elements is, by definition, sorted
    if (len(arr) <= 1):
        return arr
    # Get the middle index
    mid = len(arr) // 2
    # Divide the array into left and right sides
    left_array = arr[0:mid]
    right_array = arr[mid: len(arr)]
    # Call merge_sort on each side
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)

    return merge(sorted_left_array, sorted_right_array)
