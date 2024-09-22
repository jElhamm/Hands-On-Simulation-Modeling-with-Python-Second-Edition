# ***********************************************************************************************
#                                                                                               *
#                    Hands On Simulation Modeling with Python - Chapter 3                       *
#                                                                                               *
#       This code defines a class BinomialHistogram to generate and plot a histogram of         *
#       binomially distributed data. The class takes three parameters: N (the number of         *
#       trials), n (the number of experiments in each trial), and p (the probability of         *
#       success).                                                                               *
#                                                                                               *
#       The generate_data method uses NumPy's random.binomial function to generate N            *
#       samples from a binomial distribution, while the plot_histogram method displays a        *
#       histogram of the generated data using Matplotlib. If no data is available, the          *
#       plot_histogram method will prompt the user to generate data first.                      *
#                                                                                               *
# ***********************************************************************************************



import numpy as np
import matplotlib.pyplot as plt


class BinomialHistogram:
    def __init__(self, N, n, p):
        self.N = N
        self.n = n
        self.p = p
        self.data = None

    def generate_data(self):
        self.data = np.random.binomial(self.n, self.p, self.N)

    def plot_histogram(self):
        if self.data is None:
            print("No data available. Please generate data first.")
            return
        plt.figure()
        plt.hist(self.data, density=True, alpha=0.8, histtype='bar', color='green', ec='black')
        plt.show()


def main():
    N = 1000
    n = 10
    p = 0.5

    histogram = BinomialHistogram(N, n, p)
    histogram.generate_data()
    histogram.plot_histogram()

if __name__ == "__main__":
    main()
