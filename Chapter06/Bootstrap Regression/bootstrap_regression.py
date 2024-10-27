import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

class LinearRegressionBootstrap:
    def __init__(self, num_samples=100, n_boots=500):
        self.num_samples = num_samples
        self.n_boots = n_boots
        self.x, self.y = self.generate_data()
        self.reg_model = self.fit_model()
        self.boot_slopes = []
        self.boot_intercepts = []
        self.r_squared_values = []

    def generate_data(self):
        """Generate x and y data for linear regression."""
        x = np.linspace(0, 1, self.num_samples)
        y = x + np.random.rand(len(x))

        for _ in range(30):
            x = np.append(x, np.random.choice(x))
            y = np.append(y, np.random.choice(y))

        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)
        return x, y

    def fit_model(self):
        """Fit a linear regression model."""
        model = LinearRegression().fit(self.x, self.y)
        r_sq = model.score(self.x, self.y)
        print(f"R squared = {r_sq}")

        slope = float(model.coef_[0])
        print(f"Slope: {slope}")
        intercept = float(model.intercept_[0])
        print(f"Intercept: {intercept}")

        return model

    def bootstrap(self):
        """Perform bootstrapping to estimate slopes and intercepts."""
        data = pd.DataFrame({'x': self.x.flatten(), 'y': self.y.flatten()})

        for _ in range(self.n_boots):
            sample = data.sample(n=len(data), replace=True)
            x_temp = sample['x'].values.reshape(-1, 1)
            y_temp = sample['y'].values.reshape(-1, 1)
            reg_model = LinearRegression().fit(x_temp, y_temp)

            self.r_squared_values.append(reg_model.score(x_temp, y_temp))
            self.boot_intercepts.append(float(reg_model.intercept_[0]))
            self.boot_slopes.append(float(reg_model.coef_[0]))

            # Plot each bootstrap regression line
            y_pred_temp = reg_model.predict(x_temp)
            plt.plot(x_temp, y_pred_temp, color='grey', alpha=0.2)

    def plot_results(self):
        """Plot the original data and bootstrap regression lines."""
        y_pred = self.reg_model.predict(self.x)
        plt.scatter(self.x, self.y, label='Data Points')
        plt.plot(self.x, y_pred, linewidth=2, color='blue', label='Original Regression Line')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Linear Regression with Bootstrap')
        plt.legend()
        plt.show()

        sns.histplot(data=self.boot_slopes, kde=True, label='Bootstrapped Slopes')
        plt.title('Distribution of Bootstrapped Slopes')
        plt.show()
        
        sns.histplot(data=self.boot_intercepts, kde=True, label='Bootstrapped Intercepts')
        plt.title('Distribution of Bootstrapped Intercepts')
        plt.show()

        plt.plot(self.r_squared_values)
        plt.title('R-squared Values from Bootstraps')
        plt.xlabel('Bootstrap Iteration')
        plt.ylabel('R-squared')
        plt.show()

    def analyze_bootstrap_results(self):
        """Analyze the results of bootstrapping."""
        max_r_sq = max(self.r_squared_values)
        print(f"Max R squared = {max_r_sq}")

        pos_max_r_sq = self.r_squared_values.index(max_r_sq)
        print(f"Boot of the best Regression model = {pos_max_r_sq}")

        max_slope = self.boot_slopes[pos_max_r_sq]
        print(f"Slope of the best Regression model = {max_slope}")

        max_intercept = self.boot_intercepts[pos_max_r_sq]
        print(f"Intercept of the best Regression model = {max_intercept}")


if __name__ == "__main__":
    regression_bootstrap = LinearRegressionBootstrap()
    regression_bootstrap.bootstrap()
    regression_bootstrap.plot_results()
    regression_bootstrap.analyze_bootstrap_results()
