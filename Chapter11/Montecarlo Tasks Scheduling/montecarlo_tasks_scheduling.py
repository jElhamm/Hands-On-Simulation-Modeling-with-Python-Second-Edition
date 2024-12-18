import pandas as pd
import random
import numpy as np


class ProjectCompletionSimulator:
    def __init__(self, num_simulations=10000):
        self.num_simulations = num_simulations
        self.total_time = []
        self.task_times = [
            [3, 5, 8],
            [2, 4, 7],
            [3, 5, 9],
            [4, 6, 10],
            [3, 5, 9],
            [2, 6, 8]
        ]
        self.Lh = self.calculate_Lh()
        self.data = None

    def calculate_Lh(self):
        Lh = []
        for times in self.task_times:
            Lh.append((times[1] - times[0]) / (times[2] - times[0]))
        return Lh

    def simulate(self):
        T = np.empty(shape=(self.num_simulations, 6))
        
        for p in range(self.num_simulations):
            for i in range(6):
                trand = random.random()
                if trand < self.Lh[i]:
                    T[p][i] = self.task_times[i][0] + np.sqrt(
                        trand * (self.task_times[i][1] - self.task_times[i][0]) * (self.task_times[i][2] - self.task_times[i][0])
                    )
                else:
                    T[p][i] = self.task_times[i][2] - np.sqrt(
                        (1 - trand) * (self.task_times[i][2] - self.task_times[i][1]) * (self.task_times[i][2] - self.task_times[i][0])
                    )
            self.total_time.append(
                T[p][0] + np.maximum(T[p][1], T[p][2]) + np.maximum(T[p][3], T[p][4]) + T[p][5]
            )

        self.data = pd.DataFrame(T, columns=['Task1', 'Task2', 'Task3', 'Task4', 'Task5', 'Task6'])

    def get_statistics(self):
        return {
            "Minimum": np.amin(self.total_time),
            "Mean": np.mean(self.total_time),
            "Maximum": np.amax(self.total_time)
        }

    def display_data_description(self):
        pd.set_option('display.max_columns', None)
        print(self.data.describe())

    def plot_histogram(self):
        self.data.hist(bins=10)


if __name__ == "__main__":
    simulator = ProjectCompletionSimulator(num_simulations=10000)
    simulator.simulate()
    simulator.display_data_description()
    simulator.plot_histogram()
    stats = simulator.get_statistics()
    print("Minimum project completion time =", stats["Minimum"])
    print("Mean project completion time =", stats["Mean"])
    print("Maximum project completion time =", stats["Maximum"])
