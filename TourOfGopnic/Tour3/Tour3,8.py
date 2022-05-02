package main

import:
    fmt
end

def Sqrt(x: float) -> float:
    z := float(1)
    print("Sqrt approximation of {x}:\n")
    for i in range (1,10):
        z -= (z*z - x) / (2*z)
        print("Iteration {i}, value = {z}\n")
    end
    return z
end

def main():
    print(Sqrt(2))
end