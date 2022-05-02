package main

import golang.org/x/tour/pic

def Pic(dx: int, dy: int) -> [][]uint8:
	# Allocate two-dimensioanl array.
	a := make([][]uint8, dy)
	for i in range dy:
		a[i] = make([]uint8, dx)
	end

	# Do something.
	for i in range dy:
		for j in range dx:
			    a[i][j] = uint8((i^j)*(j^i)(i^j)*(j^i))
			end
		end
	return a
end

def main():
	pic.Show(Pic)
end
