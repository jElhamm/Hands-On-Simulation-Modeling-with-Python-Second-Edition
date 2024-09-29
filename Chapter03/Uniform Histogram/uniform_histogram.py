# ***********************************************************************************************************
#                                                                                                           *
#                          Hands On Simulation Modeling with Python - Chapter 3                             *
#                                                                                                           *
#       This code defines a class `RandomPlotter` that generates random numbers uniformly distributed       *
#       between a specified range [a, b], and then provides methods to plot these numbers. It includes      *
#       functionalities to generate a list of random numbers and visualize them using line plots and        *
#       histograms.                                                                                         *
#                                                                                                           *
#       Main Features:                                                                                      *
#       - `generate_data`: Generates N random numbers uniformly distributed between a and b.                *
#       - `plot_data`: Plots the generated random numbers as a line plot.                                   *
#       - `plot_histogram`: Plots a histogram of the generated random numbers to visualize their            *
#         distribution.                                                                                     *
#                                                                                                           *
#       Examples:                                                                                           *
#       - Example 1: Generates 100 random numbers and visualizes them with both a line plot and a           *
#         histogram.                                                                                        *
#       - Example 2: Generates 10,000 random numbers and visualizes them similarly to Example 1, but        *
#         with a larger sample size to observe the distribution more clearly.                               *
#                                                                                                           *
# ***********************************************************************************************************



import numpy as np
import matplotlib.pyplot as plt


class RandomPlotter:
    def __init__(self, a, b, N):
        self.a = a
        self.b = b
        self.N = N
        self.data = None

    def generate_data(self):
        """Generate N random numbers uniformly distributed between a and b."""
        self.data = np.random.uniform(self.a, self.b, self.N)

    def plot_data(self):
        """Plot the generated random data."""
        plt.plot(self.data)
        plt.show()

    def plot_histogram(self):
        """Plot a histogram of the generated random data."""
        plt.figure()
        plt.hist(self.data, density=True, histtype='stepfilled', alpha=0.2)
        plt.show()

def main():
    # Example 1 with N=100
    plotter1 = RandomPlotter(a=1, b=100, N=100)
    plotter1.generate_data()
    print("\n\n")
    plotter1.plot_data()
    print("\n\n")
    plotter1.plot_histogram()

    # Example 2 with N=10000
    plotter2 = RandomPlotter(a=1, b=100, N=10000)
    plotter2.generate_data()
    print("\n\n")
    plotter2.plot_data()
    print("\n\n")
    plotter2.plot_histogram()


if __name__ == "__main__":
    main()