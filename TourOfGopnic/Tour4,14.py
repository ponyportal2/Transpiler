package main

import:
	fmt
	strings
end

def main():
	# Create a tic-tac-toe board.
	board := [][]string:
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	end

	# The players take turns.
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for in range len(board):
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	end 
end
