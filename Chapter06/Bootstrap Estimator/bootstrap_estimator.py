import random
import numpy as np
import matplotlib.pyplot as plt

class BootstrapEstimator:
    def __init__(self, population_size=1000, sample_size=100, num_samples=10000):
        self.population_size = population_size
        self.sample_size = sample_size
        self.num_samples = num_samples
        self.population_data = self.generate_population()
        self.sample_data = self.take_sample()
        self.bootstrap_means = self.bootstrap_sampling()

    def generate_population(self):
        """Generate a population of random data."""
        random.seed(7)
        return [50 * random.random() for _ in range(self.population_size)]

    def take_sample(self):
        """Take a simple random sample from the population."""
        return random.choices(self.population_data, k=self.sample_size)

    def bootstrap_sampling(self):
        """Perform bootstrap sampling and calculate the means."""
        means = []
        for _ in range(self.num_samples):
            sample = random.choices(self.population_data, k=self.sample_size)
            means.append(np.mean(sample))
        return means

    def plot_bootstrap_distribution(self):
        """Plot the distribution of bootstrap sample means."""
        plt.hist(self.bootstrap_means, bins=30, edgecolor='black')
        plt.title('Bootstrap Sample Means Distribution')
        plt.xlabel('Mean')
        plt.ylabel('Frequency')
        plt.show()

    def display_results(self):
        """Print the results of the means."""
        mean_bootstrap = np.mean(self.bootstrap_means)
        mean_population = np.mean(self.population_data)
        mean_sample = np.mean(self.sample_data)

        print("The mean of the Bootstrap estimator is ", mean_bootstrap)
        print("The mean of the population is ", mean_population)
        print("The mean of the simple random sample is ", mean_sample)


if __name__ == "__main__":
    estimator = BootstrapEstimator()
    estimator.plot_bootstrap_distribution()
    estimator.display_results()
