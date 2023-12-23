package main

import (
	"algo/utils"
	"fmt"
)

func insertionSort(arr []int) []int {
	i := 1
	for i < len(arr) {
		key := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j = j - 1
		}
		arr[j+1] = key
		i++
	}
	return arr
}

func main() {
	sample_array := utils.GenerateRandomArray(300)
	fmt.Println("Random array:", sample_array)
	sorted := insertionSort(sample_array)
	fmt.Println("Sorted Array", sorted)
}
