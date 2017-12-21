package main

import (
	"fmt"
	"math"
)

func initList(n int) []int {
	l := make([]int, n)
	for i := 0; i < n; i++ {
		l[i] = i
	}
	return l
}

func reverse(l []int, s int, n int) []int {
	j := s
	length := len(l)
	numSwaps := int(math.Ceil(float64(n) / 2))
	for i := 0; i < numSwaps; i++ {
		// start + number of swaps, moving it backwards by the current swap iteration (i) - 1
		tailPos := s + n - i - 1
		a := l[tailPos%length]
		b := l[j%length]
		l[tailPos%length] = b
		l[j%length] = a
		j++
	}
	return l
}

func hash(l []int, t []int) []int {
	start := 0
	for i, val := range t {
		l = reverse(l, start, val)
		start = (val + i + start) % len(l)
	}
	return l
}

func main() {
	l := initList(256)
	trans := []int{120, 93, 0, 90, 5, 80, 129, 74, 1, 165, 204, 255, 254, 2, 50, 113}
	l = hash(l, trans)
	fmt.Printf("%v", l)
}
