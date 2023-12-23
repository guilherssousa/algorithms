package utils

import "math/rand"

func GenerateRandomArray(length int) []int {
	return rand.Perm(length)
}
