from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
from sklearn.model_selection import permutation_test_score
import matplotlib.pyplot as plt
import seaborn as sns


class PermutationTestClassifier:
    def __init__(self, n_permutations=1000, random_state=1):
        self.n_permutations = n_permutations
        self.random_state = random_state
        self.clf = tree.DecisionTreeClassifier(random_state=self.random_state)

    def load_data(self):
        """Load the Iris dataset."""
        data = load_iris()
        self.X = data.data
        self.y = data.target

    def generate_nc_data(self):
        """Generate normally distributed data that is not correlated."""
        np.random.seed(self.random_state)
        self.X_nc_data = np.random.normal(size=(len(self.X), 4))

    def perform_permutation_test(self, X, y):
        """Perform permutation test on the given data."""
        return permutation_test_score(
            self.clf, X, y, scoring="accuracy", n_permutations=self.n_permutations
        )

    def plot_histogram(self, p_test_result, title):
        """Plot histogram for permutation test results."""
        plt.figure()
        pbox = sns.histplot(data=p_test_result[1], kde=True)
        plt.axvline(p_test_result[0], linestyle="-", color='r', label='Observed Score')
        plt.axvline(p_test_result[2], linestyle="--", color='b', label='P-value')
        pbox.set(xlim=(0, 1))
        plt.title(title)
        plt.legend()
        plt.show()

    def run_tests(self):
        """Run permutation tests on both Iris and no-correlated data."""
        self.load_data()

        # Permutation test on Iris dataset
        p_test_iris = self.perform_permutation_test(self.X, self.y)
        print(f"Score of iris flower classification = {p_test_iris[0]}")
        print(f"P-value of permutation test for iris dataset = {p_test_iris[2]}")

        # Generate and test no-correlated data
        self.generate_nc_data()
        p_test_nc_data = self.perform_permutation_test(self.X_nc_data, self.y)
        print(f"Score of no-correlated data classification = {p_test_nc_data[0]}")
        print(f"P-value of permutation test for no-correlated dataset = {p_test_nc_data[2]}\n\n")

        # Plot histograms
        self.plot_histogram(p_test_iris, "Permutation Test: Iris Dataset")
        self.plot_histogram(p_test_nc_data, "Permutation Test: No-Correlated Dataset")


if __name__ == "__main__":
    classifier = PermutationTestClassifier()
    classifier.run_tests()
