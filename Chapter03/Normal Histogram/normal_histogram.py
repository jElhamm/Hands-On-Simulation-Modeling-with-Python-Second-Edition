# ***********************************************************************************************************
#                                                                                                           *
#                           Hands-On Visualization with Python - Chapter 3                                  *
#                                                                                                           *
#       This code defines a class NormalDistributionPlotter for generating and plotting normal              *
#       distributions. The class is initialized with a list of tuples, where each tuple contains            *
#       the mean (mu), standard deviation (sigma), and color for the normal distributions to be plotted.    *
#                                                                                                           *
#       The generate_data method creates samples from normal distributions based on the provided            *
#       parameters and stores them in a list. The plot_distributions method plots histograms of             *
#       these distributions with Kernel Density Estimation (KDE) using Seaborn, allowing for visual         *
#       comparison of different distributions. The histograms are plotted in multiple figures if            *
#       there are more than three distributions to ensure clarity.                                          *
#                                                                                                           *
# ***********************************************************************************************************



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class NormalDistributionPlotter:
    def __init__(self, params_list):
        """
        Initialize with a list of tuples where each tuple contains 
        (mu, sigma, color) for generating normal distributions.
        """

        self.params_list = params_list
        self.data = []

    def generate_data(self):
        """Generate normal distribution data based on provided parameters."""

        self.data = []
        for mu, sigma, _ in self.params_list:
            distribution = np.random.normal(mu, sigma, 1000)
            self.data.append(distribution)
    
    def plot_distributions(self):
        """Plot histograms of the generated distributions with KDE."""

        plt.figure(figsize=(12, 8))
        for i, (distribution, (_, _, color)) in enumerate(zip(self.data, self.params_list)):
            if i < 3:
                sns.histplot(distribution, stat="density", kde=True, color=color, label=f'Distribution {i+1}')
            else:
                plt.figure(figsize=(12, 8))
                sns.histplot(distribution, stat="density", kde=True, color=color, label=f'Distribution {i+1}')
        
        plt.legend()
        plt.show()

def main():
    params_list = [                                                           # Parameters for each normal distribution (mu, sigma, color)
        (5, 2, 'g'),
        (10, 2, 'b'),
        (15, 2, 'y'),
        (10, 2, 'g'),
        (10, 1, 'b'),
        (10, 0.5, 'y')
    ]
    plotter = NormalDistributionPlotter(params_list)                          # Create an instance of NormalDistributionPlotter
    plotter.generate_data()                                                   # Generate the data and plot the distributions
    plotter.plot_distributions()

if __name__ == "__main__":
    main()
