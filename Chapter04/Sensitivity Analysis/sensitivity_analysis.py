# ***************************************************************************************************************************
#                                                                                                                           *
#                               Hands On Simulation Modeling with Python - Chapter 4                                        *
#                                                                                                                           *
#       This code defines a class `SimpleSensitivityAnalyzer` to perform a sensitivity analysis of a given                  *
#       function by varying its parameters over specified ranges. The analysis results are collected and visualized         * 
#       using scatter plots to understand how changes in the parameters affect the function's output.                       *
#                                                                                                                           *
#       Main Features:                                                                                                      *
#       - `__init__`: Initializes the `SimpleSensitivityAnalyzer` with parameter ranges and a function to analyze.          *
#       - `perform_analysis`: Computes the function results for all combinations of parameter values. Handles               *
#         exceptions if any error occurs during function evaluation.                                                        *
#       - `plot`: Generates a scatter matrix plot of the parameter values versus the function results to visualize          *
#         relationships between parameters and the function output.                                                         *
#                                                                                                                           *
#       Example Workflow:                                                                                                   *
#       - Define parameter ranges `param_ranges` and the function `my_func` to be analyzed.                                 * 
#       - Create an instance of `SimpleSensitivityAnalyzer`.                                                                *
#       - Execute the analysis and print the results.                                                                       *
#       - Generate a scatter matrix plot of the results.                                                                    *
#                                                                                                                           *
#       Note: Ensure the function provided can handle all combinations of parameter values without errors.                  *
#                                                                                                                           *
# ***************************************************************************************************************************



import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


class SimpleSensitivityAnalyzer:
    def __init__(self, param_ranges, func):
        self.param_ranges = param_ranges
        self.func = func

    def perform_analysis(self):
        results = []
        for x_1 in self.param_ranges['x_1']:
            for x_2 in self.param_ranges['x_2']:
                for x_3 in self.param_ranges['x_3']:
                    try:
                        result = self.func(x_1, x_2, x_3)
                        results.append((x_1, x_2, x_3, result))
                    except Exception as e:
                        print(f"Error processing x_1={x_1}, x_2={x_2}, x_3={x_3}: {e}")
        
        df = pd.DataFrame(results, columns=['x_1', 'x_2', 'x_3', 'Result'])
        return df

    def plot(self, df):
        if 'Result' in df.columns:
            pd.plotting.scatter_matrix(df[['x_1', 'x_2', 'Result']], alpha=0.2, figsize=(10, 10), diagonal='kde')
            plt.show()
        else:
            print("The 'Result' column is missing from the DataFrame.")


def my_func(x_1, x_2, x_3):
    return math.log(x_1 / x_2 + x_3)


def main():
    param_ranges = {
        'x_1': np.arange(10, 100, 10),
        'x_2': np.arange(1, 10, 1),
        'x_3': np.arange(1, 10, 1)
    }
    
    analyzer = SimpleSensitivityAnalyzer(param_ranges, my_func)
    results_df = analyzer.perform_analysis()
    
    if not results_df.empty:
        print(results_df)
        analyzer.plot(results_df)
    else:
        print("No data available to plot.")


if __name__ == "__main__":
    main()
