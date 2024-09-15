# ***********************************************************************************************
#                                                                                               *
#                   Hands On Simulation Modeling with Python - Chapter 2                        *
#                                                                                               *
#       This code defines a class LinearCongruentialGenerator for generating pseudo-random      *
#       numbers using a linear congruential method with a specified modulus.                    *
#       The LinearCongruentialGenerator class has a method generate_numbers to produce a        *
#       sequence of pseudo-random numbers based on two initial seeds and a modulus value.       *
#       In the main() function, an instance of LinearCongruentialGenerator is created with      *
#       predefined parameters, and it generates 100 numbers. The generated numbers are then     *
#       printed to the console.                                                                 *
#                                                                                               *
# ***********************************************************************************************


import numpy as np


class LinearCongruentialGenerator:
    def __init__(self, seed1, seed2, modulus):
        self.x0 = seed1
        self.x1 = seed2
        self.modulus = modulus

    def generate_numbers(self, count):
        numbers = []
        for _ in range(count):
            x = np.mod((self.x0 + self.x1), self.modulus)
            numbers.append(x)
            self.x0 = self.x1
            self.x1 = x
        return numbers

def main():
    # Initialize parameters
    seed1 = 1
    seed2 = 1
    modulus = 2**32
    generator = LinearCongruentialGenerator(seed1, seed2, modulus)          # Create an instance of the generator
    numbers = generator.generate_numbers(100)                               # Generate and print numbers
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()
