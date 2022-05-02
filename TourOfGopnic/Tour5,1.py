package main

import:
	fmt
	math
end

struct Vertex:
	X: float, Y: float
end

def Vertex(v).Abs() -> float64:
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
end

# alt

def Abs(v Vertex) -> float64:
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
end

def main():
	v := Vertex{3, 4}
	print(v.Abs())
end

# alt

def main():
	v := Vertex{3, 4}
	print(Abs(v))
end
