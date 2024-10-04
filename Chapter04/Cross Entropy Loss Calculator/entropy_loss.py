# ***************************************************************************************************************
#                                                                                                               *
#                          Hands On Simulation Modeling with Python - Chapter 4                                 *
#                                                                                                               *
#       This code defines a class `CrossEntropyLossCalculator` to calculate the cross-entropy loss between      *
#       the true binary labels and the predicted probabilities in a binary classification task.                 *
#                                                                                                               *
#       Example Workflow:                                                                                       *
#       - Define the true binary labels `y` and predicted probabilities `p`.                                    *
#       - Instantiate the `CrossEntropyLossCalculator` class with the labels and predictions.                   *
#       - Call `cross_entropy_loss` to compute the average cross-entropy loss for the predictions.              *
#                                                                                                               *
# ***************************************************************************************************************



import numpy as np


class CrossEntropyLossCalculator:
    def __init__(self, y, p):
        self.y = y                                                                        # Ground truth labels
        self.p = p                                                                        # Predicted probabilities

    def cross_entropy_loss(self):
        """Calculate the cross-entropy loss."""
        ce_loss = -sum(self.y * np.log(self.p) + (1 - self.y) * np.log(1 - self.p))
        return ce_loss / len(self.p)                                                      # Normalize by the number of predictions

def main():
    y = np.array([1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0])
    p = np.array([0.8, 0.1, 0.9, 0.2, 0.8, 0.1, 0.7, 0.3, 0.6, 0.4])
    calculator = CrossEntropyLossCalculator(y, p)
    ce_loss = calculator.cross_entropy_loss()
    print("\n\n", "-"*39)
    print(f'|   Cross Entropy Loss = {ce_loss:.3f} nats' , "   |")
    print("-"*40, "\n\n")


if __name__ == "__main__":
    main()
