package main

import (
	"reflect"
	"testing"
)

func TestSampleHash(t *testing.T) {
	list := initList(5)
	knotHash := hash(list, []int{3, 4, 1, 5})
	expected := []int{3, 4, 2, 1, 0}
	if !reflect.DeepEqual(knotHash, expected) {
		t.Errorf("Expected %v, got %v", expected, knotHash)
	}
}
