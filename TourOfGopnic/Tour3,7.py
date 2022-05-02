package main

import:
	fmt
	math
end

def pow(x: float, n: float, lim: float) -> float:
	if v := math.Pow(x, n) and then v < lim:
		return v
	else:
		print("{v.g} >= {lim.g}\n", v, lim)
	end
	# can't use v here, though
	return lim
end

def main():
	print:
		pow(3, 2, 10),
		pow(3, 3, 20),
	end
end
