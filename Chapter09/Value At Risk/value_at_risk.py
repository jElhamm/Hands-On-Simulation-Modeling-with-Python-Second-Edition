import datetime as dt
import numpy as np
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm


class StockAnalysis:
    def __init__(self, stock_list, start_date, end_date):
        self.stock_list = stock_list
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = None
        self.stock_close = None
        self.stock_returns = None

    def fetch_data(self):
        self.stock_data = wb.DataReader(self.stock_list, 'yahoo', self.start_date, self.end_date)
        self.stock_close = self.stock_data["Adj Close"]
        print(self.stock_close.describe())

    def plot_stock_prices(self):
        fig, axs = plt.subplots(3, 2, figsize=(20, 10))
        for i, stock in enumerate(self.stock_list):
            row = i // 2
            col = i % 2
            axs[row, col].plot(self.stock_close[stock])
            axs[row, col].set_title(stock)
        plt.tight_layout()
        plt.show()

    def calculate_returns(self):
        self.stock_returns = self.stock_close.pct_change()
        print(self.stock_returns.tail(15))

    def calculate_var(self, portfolio_value=1000000000.00, confidence_level=0.95):
        mean_stock_ret = np.mean(self.stock_returns)
        std_stock_ret = np.std(self.stock_returns)

        working_days_2021 = 252.0
        annualized_mean_stock_ret = mean_stock_ret / working_days_2021
        annualized_std_stock_ret = std_stock_ret / np.sqrt(working_days_2021)

        INPD = norm.ppf(1 - confidence_level, annualized_mean_stock_ret, annualized_std_stock_ret)
        VaR = portfolio_value * INPD
        round_var = np.round_(VaR, 2)

        for i in range(len(self.stock_list)):
            print(f"Value-at-Risk for {self.stock_list[i]} is equal to {round_var[i]}")


def main():
	stock_list = ['ADBE', 'CSCO', 'IBM', 'NVDA', 'MSFT', 'HPQ']
	start_date = dt.datetime(2021, 1, 1)
	end_date = dt.datetime(2021, 12, 31)

	analysis = StockAnalysis(stock_list, start_date, end_date)
	analysis.fetch_data()
	analysis.plot_stock_prices()
	analysis.calculate_returns()
	analysis.calculate_var()


if __name__ == "__main__":
    main()