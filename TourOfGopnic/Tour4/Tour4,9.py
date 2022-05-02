package main

import fmt

def main():
	q := []int{2, 3, 5, 7, 11, 13}
	print(q)

	r := []bool{true, false, true, true, false, true}
	print(r)

	s := []struct:
		i int
		b bool
	end,:
		{2, true}
		{3, false}
		{5, true}
		{7, true}
		{11, false}
		{13, true}
	end
	print(s)
end
