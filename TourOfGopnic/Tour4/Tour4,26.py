package main

import fmt

def fibonacci() -> (func() -> int):
	num := []int{0, 1}

	return func() -> int:
		out := num[0]
		num[0] = num[1]
		num[1] = out + num[0]

		return out
	end
end

def main():
	f := fibonacci()
	for i in range(10):
		print(f())
	end
end