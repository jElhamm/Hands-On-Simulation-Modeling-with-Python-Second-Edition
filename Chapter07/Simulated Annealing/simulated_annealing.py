import numpy as np
import matplotlib.pyplot as plt


class SimulatedAnnealing:
    def __init__(self, temp=2000, iter=2000, step_size=0.1, seed=15):
        self.temp = temp
        self.iter = iter
        self.step_size = step_size
        self.seed = seed
        self.x = np.linspace(0, 10, 1000)
        self.cost_func_eval = []
        np.random.seed(self.seed)

    def cost_function(self, x):
        return x * np.sin(2.1 * x + 1)

    def plot_cost_function(self):
        plt.plot(self.x, self.cost_function(self.x))
        plt.xlabel('X')
        plt.ylabel('Cost Function')
        plt.show()

    def optimize(self):
        xi = np.random.uniform(min(self.x), max(self.x))
        E_xi = self.cost_function(xi)
        xit, E_xit = xi, E_xi
        acc_prob = 1

        for i in range(self.iter):
            xstep = xit + np.random.randn() * self.step_size
            E_step = self.cost_function(xstep)

            if E_step < E_xi:
                xi, E_xi = xstep, E_step
                self.cost_func_eval.append(E_xi)
                print('\nIteration =', i, 'x_min =', xi, 'Global Minimum =', E_xi,'Acceptance Probability =', acc_prob, '\n')

            diff_energy = E_step - E_xit
            t = self.temp / (i + 1)
            acc_prob = np.exp(-diff_energy / t)

            if diff_energy < 0 or np.random.randn() < acc_prob:
                xit, E_xit = xstep, E_step

        return xi, E_xi

    def plot_optimization_progress(self):
        plt.plot(self.cost_func_eval, 'bs--')
        plt.xlabel('Improvement Step')
        plt.ylabel('Cost Function Improvement')
        plt.show()


def main():
	sa = SimulatedAnnealing()
	sa.plot_cost_function()
	global_min_x, global_min_value = sa.optimize()
	sa.plot_optimization_progress()


if __name__ == "__main__":
    main()