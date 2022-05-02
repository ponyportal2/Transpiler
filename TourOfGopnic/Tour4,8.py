package main

import fmt

def main():
	names := [4]string:
		"John",
		"Paul",
		"George",
		"Ringo",
	end
	print(names)

	a := names[0:2]
	b := names[1:3]
	print(a, b)

	b[0] = "XXX"
	print(a, b)
	print(names)
end