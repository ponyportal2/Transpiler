package main

import fmt

struct Vertex:
	X: int
	Y: int
end

def main():
	print("This is {Vertex{1, 2}/%v}")
end
