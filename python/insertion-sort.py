import unittest

from utils import generate_random_array


def internet_implemented_insertion_sort(a):
    # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
        temp = a[i]

        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    return a


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        i += 1

    return arr


class SortingTest(unittest.TestCase):
    def test_insertion_sort(self):
        sample_array = [5, 1, 9, 12, 65, 0, 4, 7, 4]
        expected_array = [0, 1, 4, 4, 5, 7, 9, 12, 65]

        self.assertListEqual(insertion_sort(sample_array), expected_array)

    def test_insertion_sort_against_library(self):
        sample_array = generate_random_array(30)
        expected_array = internet_implemented_insertion_sort(sample_array.copy())

        self.assertListEqual(insertion_sort(sample_array.copy()), expected_array)


if __name__ == "__main__":
    unittest.main()
