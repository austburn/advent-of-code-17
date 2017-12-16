package main

import (
	"fmt"
	"strconv"
)

type Node struct {
	Value int
	Next  *Node
}

func initList(nodes int) Node {
	n := Node{Value: 0}
	currentNode := &n
	for i := 1; i <= nodes-1; i++ {
		next := Node{Value: i}
		currentNode.Next = &next
		currentNode = &next
	}
	currentNode.Next = &n
	return n
}

func (n Node) Len() int {
	nPtr := &n
	firstVal := n.Value
	length := 1
	for nPtr.Next != nil {
		nPtr = nPtr.Next
		if nPtr.Value == firstVal {
			break
		}
		length++
	}
	return length
}

func (n Node) Reverse() Node {
	nPtr := &n
	rev := &Node{Value: nPtr.Value}
	for nPtr.Next != nil {
		rev = &Node{Value: nPtr.Next.Value, Next: rev}
		nPtr = nPtr.Next
	}
	return *rev
}

func (n Node) String() string {
	nPtr := &n
	firstVal := n.Value
	s := "["
	for nPtr != nil {
		s += strconv.Itoa(nPtr.Value)
		nPtr = nPtr.Next

		if nPtr != nil {
			if nPtr.Value != firstVal {
				s += ", "
			} else {
				break
			}
		}
	}
	s += "]"
	return s
}

func (n Node) Split(nodes int) (Node, Node) {
	nPtr := &n
	n1 := Node{Value: nPtr.Value}
	currentNode := &n1
	for i := 0; i < nodes-1 && nPtr.Next != nil; i++ {
		nPtr = nPtr.Next
		currentNode.Next = &Node{Value: nPtr.Value}
		currentNode = currentNode.Next
	}
	currentNode.Next = nil

	if nPtr.Next != nil {
		nPtr = nPtr.Next
	} else {
		return n1, Node{}
	}

	n2 := Node{Value: nPtr.Value}
	currentNode = &n2
	for j := 0; j < n.Len()-nodes-1 && nPtr.Next != nil && nPtr.Next != &n; j++ {
		nPtr = nPtr.Next
		currentNode.Next = &Node{Value: nPtr.Value}
		currentNode = currentNode.Next
	}
	currentNode.Next = nil
	return n1, n2
}

func Append(n Node, o Node) Node {
	newNode := Node{Value: n.Value}
	currentNode := &newNode
	nPtr := &n
	for nPtr.Next != nil {
		nPtr = nPtr.Next
		next := Node{Value: nPtr.Value}
		currentNode.Next = &next
		currentNode = &next
	}

	oPtr := &o
	for oPtr.Next != nil {
		next := Node{Value: oPtr.Value}
		currentNode.Next = &next
		currentNode = &next
		oPtr = oPtr.Next
	}
	currentNode.Next = &Node{Value: oPtr.Value, Next: &n}

	return newNode
}

func KnotHash(n Node, l int) Node {
	chunk, rem := n.Split(l)
	rev := chunk.Reverse()
	hashed := Append(rev, rem)
	return hashed
}

func main() {
	l := initList(10)
	fmt.Printf("%s", l)
}
