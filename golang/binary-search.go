package main

import (
	"fmt"
)

func binarySearch(arr []int, target int) int {
	index := -1
	left := 0
	right := len(arr) - 1

	for left <= right {
		mid := (left + right) / 2

		if arr[mid] > target {
			right = mid
		}

		if arr[mid] < target {
			left = mid + 1
			index = mid
		}
	}

	return index
}

func main() {
	sample_array := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 18, 21, 25, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50}
	target := 99

	fmt.Println("Sample Array:", sample_array)
	fmt.Println("Target:", target)

	index := binarySearch(sample_array, target)
	fmt.Println("Found index:", index, sample_array[index])
}
