# ***************************************************************************************************************
#                                                                                                               *
#                          Monte Carlo Integration for Numerical Integration                                    *
#                                                                                                               *
#       This code defines a class `MonteCarloIntegrator` that uses the Monte Carlo method to estimate the       *
#       integral of a function over a given range. The Monte Carlo method is a statistical technique that       *
#       relies on random sampling to approximate complex integrals.                                             *
#                                                                                                               *
# ***************************************************************************************************************



import random
import numpy as np
import matplotlib.pyplot as plt


class MonteCarloIntegrator:
    def __init__(self, f, a, b, num_steps, num_samples):
        self.f = f                                                                          # Function to integrate
        self.a = a                                                                          # Lower limit of integration
        self.b = b                                                                          # Upper limit of integration
        self.num_steps = num_steps                                                          # Number of steps for determining ymin and ymax
        self.num_samples = num_samples                                                      # Number of Monte Carlo samples
        self.XIntegral = []                                                                 # Points inside the integral region
        self.YIntegral = []                                                                 # Corresponding y-values for points inside the region
        self.XRectangle = []                                                                # Points outside the integral region
        self.YRectangle = []                                                                # Corresponding y-values for points outside the region
        self.ymin = float('inf')
        self.ymax = float('-inf')

    def find_ymin_ymax(self):
        """Find the minimum and maximum values of f(x) over the integration range."""
        for i in range(self.num_steps):
            x = self.a + (self.b - self.a) * float(i) / self.num_steps
            y = self.f(x)
            if y < self.ymin:
                self.ymin = y
            if y > self.ymax:
                self.ymax = y

    def integrate(self):
        """Perform Monte Carlo integration."""
        A = (self.b - self.a) * (self.ymax - self.ymin)                                 # Area of the bounding rectangle
        M = 0                                                                           # Counter for points inside the region under f(x)

        # Perform the Monte Carlo sampling
        for _ in range(self.num_samples):
            x = self.a + (self.b - self.a) * random.random()
            y = self.ymin + (self.ymax - self.ymin) * random.random()
            if y <= self.f(x):
                M += 1
                self.XIntegral.append(x)
                self.YIntegral.append(y)
            else:
                self.XRectangle.append(x)
                self.YRectangle.append(y)

        return M / self.num_samples * A                                                 # Calculate the numerical integral

    def plot(self):
        """Plot the results of the Monte Carlo integration."""
        XLin = np.linspace(self.a, self.b)
        YLin = [self.f(x) for x in XLin]

        plt.axis([0, self.b, 0, self.f(self.b)])
        plt.plot(XLin, YLin, color="red", linewidth="4")                                # Function curve
        plt.scatter(self.XIntegral, self.YIntegral, color="blue", marker=".")           # Points under curve
        plt.scatter(self.XRectangle, self.YRectangle, color="yellow", marker=".")       # Points outside curve
        plt.title("Numerical Integration using Monte Carlo method")
        plt.show()

def main():
    # Define the function and the limits of integration
    f = lambda x: x**2
    a = 0.0
    b = 3.0
    num_steps = 1000000
    num_samples = 1000000

    random.seed(2)
    integrator = MonteCarloIntegrator(f, a, b, num_steps, num_samples)
    integrator.find_ymin_ymax()
    numerical_integral = integrator.integrate()
    print(f"\n\n---> Numerical integration = {numerical_integral:.6f}\n")
    integrator.plot()


if __name__ == "__main__":
    main()
