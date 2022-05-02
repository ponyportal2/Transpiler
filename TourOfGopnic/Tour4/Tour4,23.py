package main

import :
	golang.org/x/tour/wc
end

# Return a map of the counts of each “word” in the string s.

def WordCount(inputString: string) -> wordsMap map[string]int:

	wordsMap = make(map[string]int)
	SizeOfiS := len(inputString)
	j := 0
	for index in range SizeOfiS:
		# you can replace this condition with regex or multiple condition with different caracters, but the test only consider the spaces.
		if inputString[index] == ' ':
			wordsMap[inputString[:index]]++
			inputString = inputString[(index + 1):]
			SizeOfiS -= j + 1
			index -= j
			j = 0
		end
		j++
	end
	wordsMap[inputString]++
	return wordsMap
end

# The wc.Test function runs a test suite against the provided function and prints success or failure.
def main():
	wc.Test(WordCount)
end
