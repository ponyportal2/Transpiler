package main

import fmt

struct Vertex:
	Lat: float, Long: float
end

m: map[string]Vertex

def main():
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex:
		40.68433, -74.39967,
	end
	print(m["Bell Labs"])
end
