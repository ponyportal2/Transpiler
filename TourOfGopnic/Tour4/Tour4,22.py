package main

import fmt

def main():
	m := make(map[string]int)

	m["Answer"] = 42
	print("The value:", m["Answer"])

	m["Answer"] = 48
	print("The value:", m["Answer"])

	delete(m, "Answer")
	print("The value:", m["Answer"])

	v, ok := m["Answer"]
	print("The value:", v, "Present?", ok)
end
