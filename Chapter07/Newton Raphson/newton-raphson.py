import numpy as np
import matplotlib.pyplot as plt

class CubicMinimizer:
    def __init__(self, precision=0.000001, max_iter=10000, initial_x=3):
        self.precision = precision
        self.max_iter = max_iter
        self.actual_x = initial_x
        self.iteration_counter = 0

    def function(self, x):
        return x ** 3 - 2 * x ** 2 - x + 2

    def first_derivative(self, x):
        return 3 * x ** 2 - 4 * x - 1

    def second_derivative(self, x):
        return 6 * x - 4

    def plot_function(self):
        x = np.linspace(0, 3, 100)
        y = self.function(x)

        fig = plt.figure()
        axdef = fig.add_subplot(1, 1, 1)
        axdef.spines['left'].set_position('center')
        axdef.spines['bottom'].set_position('zero')
        axdef.spines['right'].set_color('none')
        axdef.spines['top'].set_color('none')
        axdef.xaxis.set_ticks_position('bottom')
        axdef.yaxis.set_ticks_position('left')

        plt.plot(x, y, 'r')
        plt.show()

        min_x = x[np.argmin(y)]
        print(f'\n\nValue of x at the minimum of the function (approx): {min_x}')

    def find_minimum(self):
        previous_step_size = 1

        while previous_step_size > self.precision and self.iteration_counter < self.max_iter:
            previous_x = self.actual_x
            self.actual_x -= self.first_derivative(previous_x) / self.second_derivative(previous_x)
            previous_step_size = abs(self.actual_x - previous_x)
            self.iteration_counter += 1
            print(f"Iteration {self.iteration_counter}: x = {self.actual_x}")

        print(f"X value of f(x) minimum (Newton's method) = {self.actual_x}")



def main():
	optimizer = CubicMinimizer()
	optimizer.plot_function()
	optimizer.find_minimum()


if __name__ == "__main__":
    main()