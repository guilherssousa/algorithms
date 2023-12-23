package main

import (
	"algo/utils"
	"fmt"
)

func bubbleSort(arr []int) []int {
	swap := false

	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				swap = true
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}

		if swap == false {
			return arr
		}
	}

	return arr
}

func main() {
	randomArray := utils.GenerateRandomArray(100)
	fmt.Println("Random Array:", randomArray)
	sorted := bubbleSort(randomArray)
	fmt.Println("Sorted Array:", sorted)
}
