import numpy as np
from sklearn.model_selection import KFold

class KFoldCrossValidator:
    def __init__(self, data, n_splits=5, shuffle=True, random_state=1):
        self.data = data
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state
        self.kfold = KFold(n_splits=self.n_splits, shuffle=self.shuffle, random_state=self.random_state)

    def perform_kfold(self):
        """Perform K-Fold cross-validation and print train and test data."""
        for train_index, test_index in self.kfold.split(self.data):
            train_data = self.data[train_index]
            test_data = self.data[test_index]
            print("Train Data:", train_data, "Test Data:", test_data)


if __name__ == "__main__":
    started_data = np.arange(10, 110, 10)
    print("Started Data:", started_data)
    kfold_validator = KFoldCrossValidator(started_data)
    kfold_validator.perform_kfold()
