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
    def __init__(self, a, c, modulus, initial_value):
        self.a = a
        self.c = c
        self.modulus = modulus
        self.x = initial_value

    def generate_values(self, count):
        values = []
        for _ in range(count):
            self.x = np.mod((self.a * self.x + self.c), self.modulus)
            values.append(self.x)
        return values

def main():
    # Initialize parameters
    a = 2
    c = 4
    modulus = 5
    initial_value = 3
    generator = LinearCongruentialGenerator(a, c, modulus, initial_value)           # Create an instance of the generator
    values = generator.generate_values(16)                                          # 16 values for range(1, 17)
    num_columns = 4                                                                 # Define the number of columns
    header = " ".join([f"{'Value':<10}"] * num_columns)
    print("\n\n")
    print(header)
    print("-" * len(header))
    for i in range(0, len(values), num_columns):                                    # Print values in a grid format
        row_values = values[i:i + num_columns]
        print(" ".join([f"{val:<10}" for val in row_values]))

    print("\n\n")


if __name__ == "__main__":
    main()