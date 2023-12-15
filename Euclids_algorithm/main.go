package main

import (
	"fmt"
)

func Euclids_algorithm(a int, b int) int {
	for a != 0 && b != 0 {
		if a > b {
			a = a % b
		} else {
			b = b % a
		}
	}

	return a + b
}

func main() {
	fmt.Println("НОД равен:", Euclids_algorithm(46, 17))
}
