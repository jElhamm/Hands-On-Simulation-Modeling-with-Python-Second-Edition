# ***************************************************************************************************************
#                                                                                                               *
#                            Hands On Simulation Modeling with Python - Chapter 3                               *
#                                                                                                               *
#       This code defines a class StatisticalPowerAnalysis to perform a power analysis for hypothesis           *
#       testing. It includes functionality to calculate the required sample size for a given effect size,       *
#       alpha level, and power, as well as calculating the statistical power for a given sample size.           *
#                                                                                                               *
#       The class also provides a method to plot power curves that show how sample size affects the power       *
#       for different effect sizes, giving a visual representation of the trade-off between sample size         *
#       and statistical power. This can be useful for planning experiments and determining appropriate          *
#       sample sizes for reliable results.                                                                      *
#                                                                                                               *
# ***************************************************************************************************************



import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.power as ssp


class StatisticalPowerAnalysis:
    def __init__(self, effect_size=0.5, alpha=0.05, power=0.8):
        """
            Initialize the power analysis with default effect size, alpha, and power values.
        """
        self.effect_size = effect_size
        self.alpha = alpha
        self.power = power
        self.stat_power = ssp.TTestPower()

    def calculate_sample_size(self):
        """
            Calculate the required sample size for the given effect size, alpha, and power.
        """
        sample_size = self.stat_power.solve_power(effect_size=self.effect_size, nobs=None, alpha=self.alpha, power=self.power)
        print('---> Sample Size: {:.2f}'.format(sample_size))
        return sample_size

    def calculate_power(self, sample_size):
        """
            Calculate the power for the given sample size, effect size, and alpha.
        """
        power = self.stat_power.solve_power(effect_size=self.effect_size, nobs=sample_size, alpha=self.alpha, power=None)
        print('\n---> Power = {:.2f}'.format(power))
        return power

    def plot_power_curve(self, effect_sizes, sample_sizes):
        """
            Plot the power curve for different effect sizes and sample sizes.
        """
        fig, ax = plt.subplots(figsize=(8, 5))
        self.stat_power.plot_power(dep_var='nobs', nobs=sample_sizes, effect_size=effect_sizes, ax=ax)
        ax.set_xlabel('Sample Size')
        ax.set_ylabel('Power')
        ax.set_title('Power Curve')
        plt.tight_layout()
        plt.show()
        plt.close(fig)

def main():
    analysis = StatisticalPowerAnalysis(effect_size=0.5, alpha=0.05, power=0.8)             # Initialize the class with default effect size, alpha, and power
    print("\n\n", "*" * 50, "\n")
    analysis.calculate_sample_size()                                                        # Calculate the required sample size
    analysis.calculate_power(sample_size=33)                                                # Calculate power for a given sample size
    print("\n", "*" * 50 , "\n")
    effect_sizes = np.array([0.2, 0.5, 0.8, 1.0])                                           # Define effect sizes and sample sizes for plotting the power curve
    sample_sizes = np.array(range(5, 500))
    analysis.plot_power_curve(effect_sizes, sample_sizes)                                   # Plot the power curve


if __name__ == "__main__":
    main()
