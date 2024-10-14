# ***********************************************************************************************************************
#                                                                                                                       *
#                                Hands On Simulation Modeling with Python - Chapter 5                                   *
#                                                                                                                       *
#       This code defines a class `RandomWalk` that simulates a one-dimensional random walk and visualizes the          *
#       path of the walk. In a random walk, each step is either +1 or -1, chosen with equal probability, and            *
#       the position at each step is updated accordingly.                                                               *
#                                                                                                                       *
# ***********************************************************************************************************************



import random
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, seed_value=1, steps=1000):
        self.seed_value = seed_value
        self.steps = steps
        self.path = []
        self.initialize_walk()
    
    def initialize_walk(self):
        random.seed(self.seed_value)
        self.path.append(-1 if random.random() < 0.5 else 1)
        for _ in range(1, self.steps):
            zn_value = -1 if random.random() < 0.5 else 1
            xn_value = self.path[-1] + zn_value
            self.path.append(xn_value)
    
    def plot_path(self):
        plt.plot(self.path)
        plt.title("Random Walk Path")
        plt.xlabel("Steps")
        plt.ylabel("Position")
        plt.show()

def main():
    rw = RandomWalk(seed_value=1, steps=1000)
    rw.plot_path()

if __name__ == "__main__":
    main()
