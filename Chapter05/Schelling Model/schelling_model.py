import matplotlib.pyplot as plt
from random import random


class Agent:
    def __init__(self, agent_type):
        self.agent_type = agent_type
        self.location = self._random_location()

    def _random_location(self):
        return random(), random()

    def euclidean_distance(self, other_agent):
        return ((self.location[0] - other_agent.location[0])**2 +
                (self.location[1] - other_agent.location[1])**2) ** 0.5

    def is_satisfied(self, agents, neighbor_count, threshold):
        distances = [(self.euclidean_distance(agent), agent) 
                     for agent in agents if agent != self]
        distances.sort()

        nearest_neighbors = [agent for _, agent in distances[:neighbor_count]]
        similar_neighbors = sum(self.agent_type == agent.agent_type for agent in nearest_neighbors)
        return similar_neighbors >= threshold

    def update_location(self, agents, neighbor_count, threshold):
        while not self.is_satisfied(agents, neighbor_count, threshold):
            self.location = self._random_location()

class Simulation:
    def __init__(self, num_agents_A, num_agents_B, neighbor_count, threshold):
        self.num_agents_A = num_agents_A
        self.num_agents_B = num_agents_B
        self.neighbor_count = neighbor_count
        self.threshold = threshold
        self.agents = self._create_agents()

    def _create_agents(self):
        agents = [Agent(0) for _ in range(self.num_agents_A)]
        agents.extend(Agent(1) for _ in range(self.num_agents_B))
        return agents

    def run(self):
        step = 0
        while True:
            self.plot_grid(step)
            print("\n")
            same_location_count = 0
            for agent in self.agents:
                old_location = agent.location
                agent.update_location(self.agents, self.neighbor_count, self.threshold)
                if agent.location == old_location:
                    same_location_count += 1

            if same_location_count == len(self.agents):
                break
            step += 1
        
        print(f'\n\n ---> Satisfied agents with {self.threshold / self.neighbor_count * 100}% of similar neighbors')

    def plot_grid(self, step):
      x_A, y_A = [], []
      x_B, y_B = [], []

      for agent in self.agents:
          x, y = agent.location
          if agent.agent_type == 0:
              x_A.append(x)
              y_A.append(y)
          else:
              x_B.append(x)
              y_B.append(y)

      fig, ax = plt.subplots(figsize=(10, 10))

      if x_A and y_A:
          ax.plot(x_A, y_A, '^', markerfacecolor='b', markersize=10, label='Type A')
      if x_B and y_B:
          ax.plot(x_B, y_B, 'o', markerfacecolor='r', markersize=10, label='Type B')

      ax.set_title(f'Step number = {step}')
      ax.legend()
      plt.show()


def main():
    num_agents_A = 500
    num_agents_B = 500
    neighbor_count = 8
    threshold = 4

    simulation = Simulation(num_agents_A, num_agents_B, neighbor_count, threshold)
    simulation.run()

if __name__ == "__main__":
    main()