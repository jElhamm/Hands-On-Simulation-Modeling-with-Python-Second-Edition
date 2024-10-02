# *************************************************************************************************************
#                                                                                                             *
#                         Hands On Simulation Modeling with Python - Chapter 4                                *
#                                                                                                             *
#       This code defines a class `SamplingSimulation` that simulates the process of extracting samples       *
#       from a population, calculating the means of those samples, and visualizing both the population        *
#       data and the sample means using histograms.                                                           *
#                                                                                                             *
#       Main Features:                                                                                        *
#       - `plot_population_histogram`: Plots a histogram of the entire population data generated from         *
#         a uniform distribution between [a, b] with N data points.                                           *
#       - `extract_samples_and_calculate_means`: Randomly extracts samples from the population,               *
#         calculates the mean of each sample, and stores these means.                                         *
#       - `plot_sample_means_histogram`: Plots a histogram of the sample means, allowing visualization        *
#         of the distribution of sample means after multiple sampling.                                        *
#                                                                                                             *
# *************************************************************************************************************



import random
import numpy as np
import matplotlib.pyplot as plt


class SamplingSimulation:
    def __init__(self, a=1, b=100, N=10000, sample_size=100, num_samples=1000):
        self.a = a
        self.b = b
        self.N = N
        self.sample_size = sample_size
        self.num_samples = num_samples
        self.DataPop = list(np.random.uniform(self.a, self.b, self.N))
        self.SamplesMeans = []

    def plot_population_histogram(self):
        plt.hist(self.DataPop, density=True, histtype='stepfilled', alpha=0.2)
        plt.title('Population Data Histogram')
        plt.show()

    def extract_samples_and_calculate_means(self):
        for _ in range(self.num_samples):
            DataExtracted = random.sample(self.DataPop, k=self.sample_size)
            DataExtractedMean = np.mean(DataExtracted)
            self.SamplesMeans.append(DataExtractedMean)

    def plot_sample_means_histogram(self):
        plt.hist(self.SamplesMeans, density=True, histtype='stepfilled', alpha=0.2)
        plt.title('Sample Means Histogram')
        plt.show()

def main():
    simulation = SamplingSimulation()
    simulation.plot_population_histogram()
    simulation.extract_samples_and_calculate_means()
    simulation.plot_sample_means_histogram()


if __name__ == "__main__":
    main()