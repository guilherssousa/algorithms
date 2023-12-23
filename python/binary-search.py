import unittest


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] > target:
            right = mid

    return -1


sample = [3, 7, 9, 11, 12, 15, 16, 18, 20]

index = binary_search(sample, 7)

print(index)


class SearchTest(unittest.TestCase):
    def test_binary_search(self):
        sample_array = [3, 7, 9, 11, 12, 15, 16, 18, 20]
        target = 7
        self.assertEqual(binary_search(sample_array, target), 1)

    def test_binary_search_will_return_negative_when_number_not_found(self):
        sample_array = [3, 7, 9, 11, 12, 15, 16, 18, 20]
        target = 8
        self.assertEqual(binary_search(sample_array, target), -1)


if __name__ == "__main__":
    unittest.main()
