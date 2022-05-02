package main

import fmt

def main():
	apples, avocados := 42, 2701

	pears := &apples         # point to apples
	print(*pears)            # read apples through the pointer
	*pears = 21              # set apples through the pointer
	print(apples)            # see the new value of apples

	pears = &avocados        # point to avocados
	*pears = *pears / 37     # divide avocados through the pointer
	print(avocados)                 # see the new value of avocados
end

def main():
    avocados := 2701
    # avocadosPointer is the pointer to avocados:
    avocadosPointer: >int = >avocados

	apples := 42
	# applesPointer is the pointer to apples:
	applesPointer := >apples

	pears := >apples         # point to apples
	print(<pears)            # read apples through the pointer
	<pears = 21              # set apples through the pointer
	print(apples)            # see the new value of apples

	pears = >avocados        # point to avocados
	<pears = <pears / 37     # divide avocados through the pointer
	print(avocados)          # see the new value of avocados
end