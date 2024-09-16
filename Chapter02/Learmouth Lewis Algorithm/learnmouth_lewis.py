# *******************************************************************************************************
#                                                                                                       *
#                   Hands On Simulation Modeling with Python - Chapter 2                                *
#                                                                                                       *
#       This code defines a class LinearCongruentialGenerator for generating pseudo-random              *
#       values using a linear congruential method with parameters for multiplier (a),                   *
#       increment (c), modulus, and an initial value.                                                   *
#       The LinearCongruentialGenerator class includes a method generate_values to produce              *
#       a sequence of pseudo-random values. Each value is computed using the linear congruential        *
#       formula and normalized by dividing by the modulus. The main() function initializes the          *
#       generator with specified parameters and generates 99 values, which are then printed to          *
#       the console.                                                                                    *
#                                                                                                       *
# *******************************************************************************************************



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
            u = self.x / self.modulus
            values.append(u)
        return values

def main():
    # Initialize parameters
    a = 75
    c = 0
    modulus = 2**31 - 1
    initial_value = 0.1
    generator = LinearCongruentialGenerator(a, c, modulus, initial_value)           # Create an instance of the generator
    values = generator.generate_values(99)                                          # 99 values for range(1, 100)
    for value in values:
        print(value)


if __name__ == "__main__":
    main()