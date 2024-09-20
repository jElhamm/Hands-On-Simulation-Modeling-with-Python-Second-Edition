# ***************************************************************************************************
#                                                                                                   *
#                       Hands On Simulation Modeling with Python - Chapter 2                        *
#                                                                                                   *
#       This code defines two classes: RandomNumberGenerator and ChiSquareTest. The                 *
#       RandomNumberGenerator class uses a linear congruential method to generate a sequence        *
#       of pseudo-random numbers, scaled to fall between 0 and 1. The generate_random_numbers       *
#       method produces a specified number of random numbers.                                       *
#                                                                                                   *
#       The ChiSquareTest class performs a chi-square goodness-of-fit test on the generated         *
#       random numbers. It divides the range [0, 1) into equal intervals, counts the number of      *
#       random numbers in each interval, and computes the chi-square statistic (V) to assess        *
#       the uniformity of the distribution. The results, including the counts in each interval      *
#       and the chi-square statistic, are displayed, and a bar chart shows the distribution of      *
#       the random numbers across intervals.                                                        *
#                                                                                                   *
# ***************************************************************************************************



import numpy as np
import matplotlib.pyplot as plt


class RandomNumberGenerator:
    def __init__(self, a=75, c=0, m=2**31 - 1, x=0.1):
        self.a = a
        self.c = c
        self.m = m
        self.x = x
        self.u = np.array([])

    def generate_random_numbers(self, n=100):
        for i in range(n):
            self.x = np.mod((self.a * self.x + self.c), self.m)
            self.u = np.append(self.u, self.x / self.m)
        return self.u


class ChiSquareTest:
    def __init__(self, u, N=100, s=20):
        self.u = u
        self.N = N
        self.s = s
        self.Ns = N / s
        self.S = np.arange(0, 1, 0.05)
        self.counts = np.empty(self.S.shape, dtype=int)
        self.V = 0

    def perform_test(self):
        for i in range(self.s):
            self.counts[i] = len(np.where((self.u >= self.S[i]) & (self.u < self.S[i] + 0.05))[0])
            self.V += (self.counts[i] - self.Ns) ** 2 / self.Ns

    def display_results(self):
        print("\n\n", "*"*50 , "\n")
        print("  R = ", self.counts)
        print("  V = ", self.V)
        print("\n","*"*50, "\n\n")

    def plot_results(self):
        Ypos = np.arange(len(self.counts))
        plt.bar(Ypos, self.counts)
        plt.show()


# Main execution
def main():
    rng = RandomNumberGenerator()
    random_numbers = rng.generate_random_numbers()

    chi_square_test = ChiSquareTest(random_numbers)
    chi_square_test.perform_test()
    chi_square_test.display_results()
    chi_square_test.plot_results()

if __name__ == "__main__":
    main()
