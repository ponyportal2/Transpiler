package main

import:
	fmt
	math
end

def compute(fn: func(float, float) -> float) -> float:
	return fn(3, 4)
end

def main():
	hypot := func(x, y float) -> float:
		return math.Sqrt(x*x + y*y)
	end
	print(hypot(5, 12))

	print(compute(hypot))
	print(compute(math.Pow))
end
