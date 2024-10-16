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
