import numpy as np
import matplotlib.pyplot as plt


class StochasticBrownianMotion:
    def __init__(self, n=1000, seed=4):
        self.n = n
        self.seed = seed
        self.sqn = 1 / np.sqrt(n)
        self.z_values = None
        self.sb_motion = []

    def generate_random_values(self):
        np.random.seed(self.seed)
        self.z_values = np.random.randn(self.n)

    def simulate(self):
        Yk = 0
        for k in range(self.n):
            Yk += self.sqn * self.z_values[k]
            self.sb_motion.append(Yk)

    def plot_motion(self):
        plt.plot(self.sb_motion)
        plt.title("Stochastic Brownian Motion Simulation")
        plt.xlabel("Step")
        plt.ylabel("Position")
        plt.show()


def main():
	simulation = StochasticBrownianMotion()
	simulation.generate_random_values()
	simulation.simulate()
	simulation.plot_motion()


if __name__ == "__main__":
    main()