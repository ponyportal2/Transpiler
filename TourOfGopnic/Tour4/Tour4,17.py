package main

import fmt

def main():
	pow := make([]int, 10)
	for i, _ in range pow:
		pow[i] = 1 << uint(i) # == 2**i
	end
	for each value in range pow:
		print("{index/%d}\n")
	end

	#or

	for _, value in range pow:
		print("{index/%d}\n")
	end


end
