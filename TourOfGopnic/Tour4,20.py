package main

import fmt

struct Vertex:
	Lat: float, Long: float
end

m := map[string]Vertex:
	"Bell Labs":
		40.68433, -74.39967,
	end,
	"Google":
		37.42202, -122.08408,
	end,
end

def main():
	print(m)
end
