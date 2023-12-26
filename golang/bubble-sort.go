package main

import (
	"algo/utils"
	"fmt"
	"os"
	"strconv"
	"time"
)

func bubbleSort(arr []int) []int {
	if len(arr) == 1 {
		return arr
	}

	swap := false
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap = true
			}
		}

		if swap != true {
			return arr
		}
	}

	return arr
}

func main() {
	sample_size := 100
	if len(os.Args) > 1 {
		size, err := strconv.Atoi(os.Args[1])
		if err != nil {
			fmt.Errorf("you did some shit", err)
		}
		sample_size = size
	}

	randomArray := utils.GenerateRandomArray(sample_size)

	start := time.Now()
	bubbleSort(randomArray)
	end := time.Now()

	elapsed := end.Sub(start)

	fmt.Printf("Elapsed time: %v\n", elapsed)
}
