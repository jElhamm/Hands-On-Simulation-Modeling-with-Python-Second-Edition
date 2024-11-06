import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture


class GaussianMixtureModeling:
    def __init__(self, mean_1=25, st_1=9, mean_2=50, st_2=5, size_1=3000, size_2=7000):
        self.mean_1 = mean_1
        self.st_1 = st_1
        self.mean_2 = mean_2
        self.st_2 = st_2
        self.size_1 = size_1
        self.size_2 = size_2
        self.dist_merged = None
        self.gm_model = None
        self.dist_labels = None

    def generate_data(self):
        n_dist_1 = np.random.normal(loc=self.mean_1, scale=self.st_1, size=self.size_1)
        n_dist_2 = np.random.normal(loc=self.mean_2, scale=self.st_2, size=self.size_2)
        self.dist_merged = np.hstack((n_dist_1, n_dist_2))
        return self.dist_merged

    def plot_initial_distribution(self):
        sns.set_style("white")
        sns.histplot(data=self.dist_merged, kde=True)
        plt.show()

    def fit_gaussian_mixture(self, n_components=2, init_params='kmeans'):
        dist_merged_res = self.dist_merged.reshape((len(self.dist_merged), 1))
        self.gm_model = GaussianMixture(n_components=n_components, init_params=init_params)
        self.gm_model.fit(dist_merged_res)
        self.dist_labels = self.gm_model.predict(dist_merged_res)
        return self.gm_model

    def print_parameters(self):
        print(f"\n\nInitial distribution means = {self.mean_1, self.mean_2}")
        print(f"Initial distribution standard deviations = {self.st_1, self.st_2}")
        print(f"GM_model distribution means = {self.gm_model.means_.flatten()}")
        print(f"GM_model distribution standard deviations = {np.sqrt(self.gm_model.covariances_).flatten()}\n\n")

    def plot_fitted_distribution(self):
        sns.set_style("white")
        data_pred = pd.DataFrame({'data': self.dist_merged, 'label': self.dist_labels})
        sns.histplot(data=data_pred, x="data", kde=True, hue="label")
        plt.show()

    def plot_initial_labels(self):
        label_0 = np.zeros(self.size_1, dtype=int)
        label_1 = np.ones(self.size_2, dtype=int)
        labels_merged = np.hstack((label_0, label_1))
        data_init = pd.DataFrame({'data': self.dist_merged, 'label': labels_merged})
        sns.set_style("white")
        sns.histplot(data=data_init, x="data", kde=True, hue="label")
        plt.show()



def main():
	modeling = GaussianMixtureModeling()
	modeling.generate_data()
	modeling.plot_initial_distribution()
	modeling.fit_gaussian_mixture()
	modeling.print_parameters()
	modeling.plot_fitted_distribution()
	modeling.plot_initial_labels()


if __name__ == "__main__":
    main()