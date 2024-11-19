import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from gplearn.genetic import SymbolicRegressor


class SymbolicRegressionModel:
    def __init__(self, function_set, population_size=1000, generations=10, stopping_criteria=0.001,
                 p_crossover=0.7, p_subtree_mutation=0.1, p_hoist_mutation=0.05, p_point_mutation=0.1,
                 max_samples=0.9, parsimony_coefficient=0.01, random_state=1):
        self.function_set = function_set
        self.population_size = population_size
        self.generations = generations
        self.stopping_criteria = stopping_criteria
        self.p_crossover = p_crossover
        self.p_subtree_mutation = p_subtree_mutation
        self.p_hoist_mutation = p_hoist_mutation
        self.p_point_mutation = p_point_mutation
        self.max_samples = max_samples
        self.parsimony_coefficient = parsimony_coefficient
        self.random_state = random_state
        self.model = None

    def generate_data(self):
        x = np.arange(-1, 1, 1/10.)
        y = np.arange(-1, 1, 1/10.)
        x, y = np.meshgrid(x, y)
        f_values = x**2 + y**2
        input_train = np.random.uniform(-1, 1, 200).reshape(100, 2)
        output_train = input_train[:, 0]**2 + input_train[:, 1]**2
        input_test = np.random.uniform(-1, 1, 200).reshape(100, 2)
        output_test = input_test[:, 0]**2 + input_test[:, 1]**2
        return x, y, f_values, input_train, output_train, input_test, output_test

    def create_model(self):
        self.model = SymbolicRegressor(
            population_size=self.population_size,
            function_set=self.function_set,
            generations=self.generations,
            stopping_criteria=self.stopping_criteria,
            p_crossover=self.p_crossover,
            p_subtree_mutation=self.p_subtree_mutation,
            p_hoist_mutation=self.p_hoist_mutation,
            p_point_mutation=self.p_point_mutation,
            max_samples=self.max_samples,
            verbose=1,
            parsimony_coefficient=self.parsimony_coefficient,
            random_state=self.random_state
        )

    def fit_model(self, input_train, output_train):
        if self.model is None:
            self.create_model()
        self.model.fit(input_train, output_train)
    
    def evaluate_model(self, input_test, output_test):
        r2_score = self.model.score(input_test, output_test)
        print("Trained Model Program:", self.model._program)
        print("R2 Score:", r2_score)
        return r2_score

    def plot_surface(self, x, y, f_values):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, f_values, cmap='viridis')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


def main():
	function_set = ['add', 'sub', 'mul']
	symbolic_regression = SymbolicRegressionModel(function_set=function_set)
	x, y, f_values, input_train, output_train, input_test, output_test = symbolic_regression.generate_data()
	symbolic_regression.plot_surface(x, y, f_values)
	symbolic_regression.create_model()
	symbolic_regression.fit_model(input_train, output_train)
	symbolic_regression.evaluate_model(input_test, output_test)


if __name__ == "__main__":
    main()