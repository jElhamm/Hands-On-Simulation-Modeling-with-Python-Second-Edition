# *******************************************************************************************************************
#                                                                                                                   *
#                           Hands On Simulation Modeling with Python - Chapter 4                                    *
#                                                                                                                   *
#       This code defines a class `EntropyCalculator` that can:                                                     *
#       - Plot the probability distributions of two sets of probabilities, P and Q.                                 *
#       - Calculate the cross-entropy between two probability distributions P and Q, using the formula:             *
#         H(P, Q) = - Σ (P(x) * log2(Q(x))), where P(x) and Q(x) are the probabilities of the events.               *
#                                                                                                                   *
#       Main Features:                                                                                              *
#       - `plot_distributions`: Displays bar charts of the probability distributions P and Q for comparison.        *
#       - `cross_entropy`: Calculates and returns the cross-entropy value between the two distributions.            *
#                                                                                                                   *
#       Example Workflow:                                                                                           *
#       - Define a set of events (e.g., A, B, C, D) and their corresponding probabilities in distributions          *
#         P and Q.                                                                                                  *
#       - Instantiate the `EntropyCalculator` class with the events, P, and Q.                                      *
#       - Plot the probability distributions P and Q using `plot_distributions`.                                    *
#       - Calculate the cross-entropy between P and Q using `cross_entropy`.                                        *
#                                                                                                                   *
# *******************************************************************************************************************



from matplotlib import pyplot as plt
from math import log2


class EntropyCalculator:
    def __init__(self, events, p, q):
        self.events = events
        self.p = p
        self.q = q
        print(f'\n\n---> P = {sum(self.p):.3f}', f'\n---> Q = {sum(self.q):.3f}\n')

    def plot_distributions(self):
        plt.subplot(2, 1, 1)
        plt.bar(self.events, self.p)
        plt.title("Distribution P")
        
        plt.subplot(2, 1, 2)
        plt.bar(self.events, self.q)
        plt.title("Distribution Q")
        
        plt.tight_layout()
        plt.show()

    def cross_entropy(self):
        return -sum([p * log2(q) for p, q in zip(self.p, self.q)])

def main():
    events = ['A', 'B', 'C', 'D']
    p = [0.70, 0.05, 0.10, 0.15]
    q = [0.45, 0.10, 0.20, 0.25]
    calculator = EntropyCalculator(events, p, q)
    calculator.plot_distributions()
    h_pq = calculator.cross_entropy()
    print(f'\n---> H(P, Q) = {h_pq:.3f} bits')


if __name__ == "__main__":
    main()