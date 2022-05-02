package main

import fmt

struct Vertex:
	X: int
	Y: int
end

def main():
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println("ass{v.X/%v}")
end
