import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


class StockPriceSimulation:
    def __init__(self, file_path, num_intervals=2515, iterations=20):
        self.file_path = file_path
        self.num_intervals = num_intervals
        self.iterations = iterations
        self.stock_data = None
        self.log_returns = None
        self.drift = None
        self.daily_returns = None
        self.stock_prices = None

    def load_data(self):
        self.stock_data = pd.read_csv(self.file_path, header=0, usecols=['Date', 'Close'],
                                      parse_dates=True, index_col='Date')
        print(self.stock_data.info())
        print(self.stock_data.head())
        print(self.stock_data.tail())
        print(self.stock_data.describe())

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.stock_data)
        plt.show()

    def calculate_log_returns(self):
        pct_change = self.stock_data.pct_change()
        self.log_returns = np.log(1 + pct_change)
        print(self.log_returns.tail(10))

        plt.figure(figsize=(10, 5))
        plt.plot(self.log_returns)
        plt.show()

    def calculate_drift(self):
        mean_log_returns = np.array(self.log_returns.mean())
        var_log_returns = np.array(self.log_returns.var())
        stdev_log_returns = np.array(self.log_returns.std())
        self.drift = mean_log_returns - (0.5 * var_log_returns)
        print("Drift = ", self.drift)

    def simulate_prices(self):
        np.random.seed(7)
        sb_motion = norm.ppf(np.random.rand(self.num_intervals, self.iterations))
        self.daily_returns = np.exp(self.drift + self.log_returns.std() * sb_motion)

        start_price = self.stock_data.iloc[0]
        self.stock_prices = np.zeros_like(self.daily_returns)
        self.stock_prices[0] = start_price

        for t in range(1, self.num_intervals):
            self.stock_prices[t] = self.stock_prices[t - 1] * self.daily_returns[t]

    def plot_simulation(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.stock_prices)
        amzn_trend = np.array(self.stock_data.iloc[:, 0:1])
        plt.plot(amzn_trend, 'k*')
        plt.show()


def main():
	file_path = 'AMZN.csv'
	simulation = StockPriceSimulation(file_path)
	simulation.load_data()
	simulation.plot_data()
	simulation.calculate_log_returns()
	simulation.calculate_drift()
	simulation.simulate_prices()
	simulation.plot_simulation()


if __name__ == "__main__":
    main()