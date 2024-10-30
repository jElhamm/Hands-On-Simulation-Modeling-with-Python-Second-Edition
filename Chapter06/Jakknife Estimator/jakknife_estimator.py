import random
import statistics 
import matplotlib.pyplot as plt

class JackknifeVarianceEstimator:
    def __init__(self, population_size=100, seed=5):
        self.population_size = population_size
        self.seed = seed
        self.pop_data = self.generate_population_data()
        self.cv_pop_data = self.calculate_coefficient_of_variation(self.pop_data)
        print(f"Coefficient of Variation for Population Data: {self.cv_pop_data}")

    def generate_population_data(self):
        """Generate population data."""
        random.seed(self.seed)
        return [10 * random.random() for _ in range(self.population_size)]

    def calculate_coefficient_of_variation(self, data):
        """Calculate the coefficient of variation (CV)."""
        return statistics.stdev(data) / statistics.mean(data)

    def jackknife_variance_estimation(self):
        """Perform jackknife resampling and calculate pseudo values."""
        N = len(self.pop_data)
        jack_val = [0] * (N - 1)
        pseudo_val = [0] * N

        for i in range(N):
            for j in range(N):
                if j < i:
                    jack_val[j] = self.pop_data[j]
                elif j > i:
                    jack_val[j - 1] = self.pop_data[j]
            pseudo_val[i] = N * self.calculate_coefficient_of_variation(self.pop_data) - (N - 1) * self.calculate_coefficient_of_variation(jack_val)

        return pseudo_val

    def plot_pseudo_values(self, pseudo_val):
        """Plot the histogram of pseudo values."""
        plt.hist(pseudo_val, bins=10, alpha=0.7)
        plt.title('Histogram of Pseudo Values')
        plt.xlabel('Pseudo Value')
        plt.ylabel('Frequency')
        plt.show()

    def analyze_pseudo_values(self, pseudo_val):
        """Analyze pseudo values: mean, variance, and jackknife variance."""
        mean_pseudo_val = statistics.mean(pseudo_val)
        variance_pseudo_val = statistics.variance(pseudo_val)
        var_jack = variance_pseudo_val / len(pseudo_val)

        print(f"Mean of Pseudo Values: {mean_pseudo_val}")
        print(f"Variance of Pseudo Values: {variance_pseudo_val}")
        print(f"Jackknife Variance: {var_jack}")


if __name__ == "__main__":
    estimator = JackknifeVarianceEstimator()
    pseudo_values = estimator.jackknife_variance_estimation()
    estimator.plot_pseudo_values(pseudo_values)
    estimator.analyze_pseudo_values(pseudo_values)
