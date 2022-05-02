package main

import fmt

def main():
	s := []int{2, 3, 5, 7, 11, 13}

	s = s[1:4]
	print(s)

	s = s[:2]
	print(s)

	s = s[1:]
	print(s)
end
