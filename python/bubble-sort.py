import unittest

from utils import generate_random_array


def internet_implemented_bubble_sort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return arr
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


class SortingTest(unittest.TestCase):
    def test_bubble_sort(self):
        sample_array = [5, 1, 9, 12, 65, 0, 4, 7, 4]
        expected_array = [0, 1, 4, 4, 5, 7, 9, 12, 65]

        self.assertListEqual(bubble_sort(sample_array), expected_array)

    def test_bubble_sort_against_library(self):
        sample_array = generate_random_array(1000)
        expected_array = internet_implemented_bubble_sort(sample_array.copy())

        self.assertListEqual(bubble_sort(sample_array.copy()), expected_array)


sample_array = generate_random_array(1000)
print("Random array:", sample_array)

sorted_array = bubble_sort(sample_array)
print("Sorted array:", sorted_array)

if __name__ == "__main__":
    unittest.main()
