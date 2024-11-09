import numpy as np
import matplotlib.pyplot as plt

class QuadraticMinimizer:
    def __init__(self, learning_rate=0.01, precision=0.000001, max_iter=10000, initial_x=3):
        self.learning_rate = learning_rate
        self.precision = precision
        self.max_iter = max_iter
        self.actual_x = initial_x
        self.iteration_counter = 0
    
    def function(self, x):
        return x ** 2 - 2 * x + 1
    
    def gradient(self, x):
        return 2 * x - 2
    
    def plot_function(self):
        x = np.linspace(-1, 3, 100)
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
    
    def minimize(self):
        previous_step_size = 1
        
        while previous_step_size > self.precision and self.iteration_counter < self.max_iter:
            previous_x = self.actual_x
            self.actual_x -= self.learning_rate * self.gradient(previous_x)
            previous_step_size = abs(self.actual_x - previous_x)
            self.iteration_counter += 1
            print(f"Iteration {self.iteration_counter}: x = {self.actual_x}")
        
        print(f"Minimum of f(x) is approximately at x = {self.actual_x}")


def main():
	optimizer = QuadraticMinimizer()
	optimizer.plot_function()
	optimizer.minimize()


if __name__ == "__main__":
    main()