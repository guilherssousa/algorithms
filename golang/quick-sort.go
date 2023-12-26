package main

import (
	"algo/utils"
	"fmt"
	"os"
	"strconv"
	"time"
)

func qs(list []int, lo int, hi int) {
	if lo >= hi {
		return
	}

	partitionIndex := partition(list, lo, hi)

	qs(list, lo, partitionIndex-1)
	qs(list, partitionIndex+1, hi)
}

func partition(list []int, lo int, hi int) int {
	pivot := list[hi]

	index := lo - 1

	for i := lo; i < hi; i++ {
		if list[i] <= pivot {
			index++
			tmp := list[i]
			list[i] = list[index]
			list[index] = tmp
		}
	}

	index++
	list[hi] = list[index]
	list[index] = pivot

	return index
}

func quick_sort(list []int) {
	qs(list, 0, len(list)-1)
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

	sample := utils.GenerateRandomArray(sample_size)

	start := time.Now()
	quick_sort(sample)
	finish := time.Now()

	elapsed := finish.Sub(start)
	fmt.Printf("Executed in %v\n", elapsed)
}
