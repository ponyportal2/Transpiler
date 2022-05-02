package main

import fmt

def adder() -> (func(x: int) -> int):
	sum := 0
	return func(x: int) -> int:
		sum += x
		return sum
	end
end

def int_seq() -> (func() -> int):
	i := 0
	return def() -> int:
		i++
		return i
	end
end

def main():
	pos, neg := adder(), adder()
	for i in range 10:
		print(
			pos(i),
			neg(-2*i),
		)
	end
end

def int_seq() -> (func() -> int):
    outer::
        for i in range(5):
        inner::
            for i in range(5):
                if i == 4:
                    continue outer
                end
                if i == 6:
                    continue inner
                end
            end
        end
    end