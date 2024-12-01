import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class AirfoilNoiseModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.ASNNames = ['Frequency', 'AngleAttack', 'ChordLength', 'FSVelox', 'SSDT', 'SSP']
        self.ASNData = self.load_data()
        self.ASNDataScaled = None
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None
        self.linear_model = None
        self.mlp_model = None

    def load_data(self):
        data = pd.read_csv(self.data_path, delim_whitespace=True, names=self.ASNNames)
        print(data.head(20))
        print(data.info())
        return data

    def basic_statistics(self):
        basic_stats = self.ASNData.describe().transpose()
        print(basic_stats)

    def preprocess_data(self):
        scaler = MinMaxScaler()
        self.ASNDataScaled = scaler.fit_transform(self.ASNData)
        self.ASNDataScaled = pd.DataFrame(self.ASNDataScaled, columns=self.ASNNames)
        summary = self.ASNDataScaled.describe().transpose()
        print(summary)

    def visualize_data(self):
        boxplot = self.ASNDataScaled.boxplot(column=self.ASNNames)
        plt.show()

        correlation = self.ASNDataScaled.corr(method='pearson')
        with pd.option_context('display.max_rows', None, 'display.max_columns', correlation.shape[1]):
            print(correlation)

        plt.matshow(correlation)
        plt.xticks(range(len(correlation.columns)), correlation.columns)
        plt.yticks(range(len(correlation.columns)), correlation.columns)
        plt.colorbar()
        plt.show()

    def split_data(self):
        X = self.ASNDataScaled.drop('SSP', axis=1)
        Y = self.ASNDataScaled['SSP']
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size=0.30, random_state=5)
        print('X train shape =', self.X_train.shape)
        print('X test shape =', self.X_test.shape)
        print('Y train shape =', self.Y_train.shape)
        print('Y test shape =', self.Y_test.shape)

    def train_linear_model(self):
        self.linear_model = LinearRegression()
        self.linear_model.fit(self.X_train, self.Y_train)
        Y_predLM = self.linear_model.predict(self.X_test)
        mseLM = mean_squared_error(self.Y_test, Y_predLM)
        print('Linear Regression Model Mean Squared Error:', mseLM)

    def train_mlp_model(self):
        self.mlp_model = MLPRegressor(hidden_layer_sizes=(50), activation='relu', solver='lbfgs',
                                       tol=1e-4, max_iter=10000, random_state=1)
        self.mlp_model.fit(self.X_train, self.Y_train)
        Y_predMLPReg = self.mlp_model.predict(self.X_test)
        mseMLP = mean_squared_error(self.Y_test, Y_predMLPReg)
        print('SKLearn Neural Network Model Mean Squared Error:', mseMLP)

        plt.figure(1)
        plt.subplot(121)
        plt.scatter(self.Y_test, Y_predMLPReg)
        plt.plot((0, 1), "r--")
        plt.xlabel("Actual values")
        plt.ylabel("Predicted values")
        plt.title("SKLearn Neural Network Model")

        plt.subplot(122)
        Y_predLM = self.linear_model.predict(self.X_test)
        plt.scatter(self.Y_test, Y_predLM)
        plt.plot((0, 1), "r--")
        plt.xlabel("Actual values")
        plt.ylabel("Predicted values")
        plt.title("SKLearn Linear Regression Model")
        plt.show()


if __name__ == "__main__":
    model = AirfoilNoiseModel('airfoil_self_noise.dat')
    model.basic_statistics()
    model.preprocess_data()
    model.visualize_data()
    model.split_data()
    model.train_linear_model()
    model.train_mlp_model()
