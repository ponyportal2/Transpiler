package main

import fmt

pow := []int{1, 2, 4, 8, 16, 32, 64, 128}

def main():
	for index, value in range pow {
		fmt.Printf("2**%d = %d\n", index, value)
	end
end
