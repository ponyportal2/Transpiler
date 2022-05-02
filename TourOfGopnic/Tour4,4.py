package main

import fmt

struct Vertex:
	X: int
	Y: int
end

def main():
	v := Vertex{1, 2}
	p := >v
	p.X = 1e9
	print(v)
end
