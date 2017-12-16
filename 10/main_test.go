package main

import (
	"fmt"
	"testing"
)

var (
	singleNode = Node{
		Value: 0,
		Next:  nil,
	}

	twoNodes = Node{
		Value: 0,
		Next: &Node{
			Value: 1,
			Next:  nil,
		},
	}

	fiveNodes = Node{
		Value: 0,
		Next: &Node{
			Value: 1,
			Next: &Node{
				Value: 2,
				Next: &Node{
					Value: 3,
					Next: &Node{
						Value: 4,
						Next:  nil,
					},
				},
			},
		},
	}
)

func TestLength(t *testing.T) {
	t.Run("single node", func(tt *testing.T) {
		if singleNode.Len() != 1 {
			tt.Fatalf("Expected Length to be 1, got %d", singleNode.Len())
		}
		if fmt.Sprintf("%s", singleNode) != "[0]" {
			tt.Fatal("Expected [0]")
		}
	})

	t.Run("two nodes", func(tt *testing.T) {
		if twoNodes.Len() != 2 {
			tt.Fatalf("Expected Len to be 2, got %d", twoNodes.Len())
		}
		if fmt.Sprintf("%s", twoNodes) != "[0, 1]" {
			tt.Fatalf("Expected [0, 1], got %s", fmt.Sprintf("%s", twoNodes))
		}
		if twoNodes.Value != 0 {
			tt.Fatalf("Expected Value to not change, got %d", twoNodes.Value)
		}
	})

	t.Run("five nodes", func(tt *testing.T) {
		nodes := initList(5)
		if nodes.Len() != 5 {
			tt.Fatalf("Expected Len to be 5, got %d", nodes.Len())
		}
		if fmt.Sprintf("%s", nodes) != "[0, 1, 2, 3, 4]" {
			tt.Fatal("Expected [0, 1, 2, 3, 4], got %s", fmt.Sprintf("%s", nodes))
		}
		if nodes.Value != 0 {
			tt.Fatalf("Expected Value to not change, got %d", nodes.Value)
		}
	})

}

func TestReverse(t *testing.T) {
	t.Run("single node", func(tt *testing.T) {
		rev := singleNode.Reverse()
		if rev.Len() != 1 {
			tt.Fatalf("Expected Len to be 1, got %d", rev.Len())
		}
		if fmt.Sprintf("%s", rev) != "[0]" {
			tt.Fatalf("Expected [0], got %s", fmt.Sprintf("%s", rev))
		}
	})

	t.Run("two nodes", func(tt *testing.T) {
		rev := twoNodes.Reverse()
		if rev.Len() != 2 {
			tt.Fatalf("Expected Len to be 2, got %d", rev.Len())
		}
		if fmt.Sprintf("%s", rev) != "[1, 0]" {
			tt.Fatalf("Expected [1, 0], got %s", fmt.Sprintf("%s", rev))
		}
	})

	t.Run("five nodes", func(tt *testing.T) {
		rev := fiveNodes.Reverse()
		if rev.Len() != 5 {
			tt.Fatalf("Expected Len to be 5, got %d", rev.Len())
		}
		if fmt.Sprintf("%s", rev) != "[4, 3, 2, 1, 0]" {
			tt.Fatalf("Expected [4, 3, 2, 1, 0], got %s", fmt.Sprintf("%s", rev))
		}
	})
}

func TestSplit(t *testing.T) {
	t.Run("single node", func(tt *testing.T) {
		chunk, rem := singleNode.Split(1)
		if rem.Value != 0 && rem.Next != nil {
			tt.Fatal("Expected rem to be nil")
		}
		if chunk.Len() != 1 {
			tt.Fatalf("Expected Len to be 1, got %d", chunk.Len())
		}
		if fmt.Sprintf("%s", chunk) != "[0]" {
			tt.Fatalf("Expected [0], got %s", fmt.Sprintf("%s", chunk))
		}
	})

	t.Run("two nodes", func(tt *testing.T) {
		chunk, rem := initList(2).Split(1)
		if chunk.Len() != 1 {
			tt.Fatalf("Expected Len to be 1, got %d", chunk.Len())
		}
		if rem.Value != 1 {
			tt.Fatalf("Expected Value to be 1, got %d", rem.Value)
		}
		if fmt.Sprintf("%s", chunk) != "[0]" {
			tt.Fatalf("Expected [0], got %s", fmt.Sprintf("%s", chunk))
		}
		if fmt.Sprintf("%s", rem) != "[1]" {
			tt.Fatalf("Expected [1], got %s", fmt.Sprintf("%s", rem))
		}
	})

	t.Run("five nodes", func(tt *testing.T) {
		chunk, rem := initList(5).Split(3)
		if chunk.Len() != 3 {
			tt.Fatalf("Expected Len to be 3, got %d", chunk.Len())
		}
		if rem.Value != 3 {
			tt.Fatalf("Expected Value to be 3, got %d", rem.Value)
		}
		if fmt.Sprintf("%s", chunk) != "[0, 1, 2]" {
			tt.Fatalf("Expected [0, 1, 2], got %s", fmt.Sprintf("%s", chunk))
		}
		if fmt.Sprintf("%s", rem) != "[3, 4]" {
			tt.Fatalf("Expected [3, 4], got %s", fmt.Sprintf("%s", rem))
		}
	})

	t.Run("circular list", func(tt *testing.T) {
		l := initList(20)
		chunk, rem := l.Split(10)
		if fmt.Sprintf("%s", chunk) != "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]" {
			tt.Fatalf("Expected [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], got %s", fmt.Sprintf("%s", chunk))
		}
		if rem.Value != 10 {
			tt.Fatalf("Expected Value to be 10, got %d", rem.Value)
		}
	})
}

func TestKnotHash(t *testing.T) {
	hash := KnotHash(initList(5), 3)
	if fmt.Sprintf("%s", hash) != "[2, 1, 0, 3, 4]" {
		t.Fatalf("Expected [2, 1, 0, 3, 4], got %s", fmt.Sprintf("%s", hash))
	}
}
