# *******************************************************************************************************************************
#                                                                                                                               *
#                                Hands On Simulation Modeling with Python - Chapter 4                                           *
#                                                                                                                               *
#       This code defines a class `MonteCarloPiEstimator` to estimate the value of Pi (π) using the Monte Carlo                 *
#       method. By randomly sampling points within a unit square and determining how many fall inside a unit circle,            *
#       the value of Pi is estimated based on the ratio of points inside the circle to the total number of points.              *
#                                                                                                                               *
#       Main Features:                                                                                                          *
#       - `__init__`: Initializes the `MonteCarloPiEstimator` with the number of samples to generate. Sets up counters          *
#         and lists for storing points within the circle and the square.                                                        *
#       - `estimate_pi`: Generates random points within the unit square, checks if they fall inside the unit circle,            *
#         and estimates Pi based on the ratio of points inside the circle to the total number of points.                        *
#       - `plot_results`: Visualizes the estimation process by plotting points within the unit circle and square.               *
#         A red curve represents the boundary of the unit circle.                                                               *
#                                                                                                                               *
# *******************************************************************************************************************************



import math
import random
import numpy as np
import matplotlib.pyplot as plt


class MonteCarloPiEstimator:
    def __init__(self, num_samples):
        self.num_samples = num_samples
        self.m = 0
        self.x_circle = []
        self.y_circle = []
        self.x_square = []
        self.y_square = []

    def estimate_pi(self):
        for _ in range(self.num_samples):
            x = random.random()
            y = random.random()
            if x**2 + y**2 <= 1:
                self.m += 1
                self.x_circle.append(x)
                self.y_circle.append(y)
            else:
                self.x_square.append(x)
                self.y_square.append(y)
        
        pi_estimate = 4 * self.m / self.num_samples
        return pi_estimate

    def plot_results(self):
        xl = np.linspace(0, 1)
        yl = [math.sqrt(1 - x**2) for x in xl]
        plt.axis("equal")
        plt.grid(which="major")
        plt.plot(xl, yl, color="red", linewidth="4")
        plt.scatter(self.x_circle, self.y_circle, color="yellow", marker=".")
        plt.scatter(self.x_square, self.y_square, color="blue", marker=".")
        plt.title("Monte Carlo method for Pi estimation")
        plt.show()

def main():
    num_samples = 10000
    estimator = MonteCarloPiEstimator(num_samples)
    pi_estimate = estimator.estimate_pi()
    print(f"\n\n---> N={num_samples} \n---> M={estimator.m} \n---> Pi={pi_estimate:.2f}\n")
    estimator.plot_results()


if __name__ == "__main__":
    main()
