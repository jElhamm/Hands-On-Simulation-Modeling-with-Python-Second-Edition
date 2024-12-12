import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score


class ConcreteModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.features_names = ['Cement', 'BFS', 'FLA', 'Water', 'SP', 'CA', 'FA', 'Age', 'CCS']
        self.concrete_data = self.load_data()
        self.scaled_data = None
        self.model = None

    def load_data(self):
        data = pd.read_excel(self.data_path, names=self.features_names)
        print(data.describe())
        return data

    def visualize_data(self):
        sns.set(style="ticks")
        sns.boxplot(data=self.concrete_data)
        sns.boxplot(data=self.scaled_data)

    def preprocess_data(self):
        scaler = MinMaxScaler()
        self.scaled_data = scaler.fit_transform(self.concrete_data)
        self.scaled_data = pd.DataFrame(self.scaled_data, columns=self.features_names)
        print(self.scaled_data.describe())

    def split_data(self):
        input_data = self.scaled_data.iloc[:, :8]
        output_data = self.scaled_data.iloc[:, 8]
        self.inp_train, self.inp_test, self.out_train, self.out_test = train_test_split(
            input_data, output_data, test_size=0.30, random_state=1
        )
        print(self.inp_train.shape, self.inp_test.shape, self.out_train.shape, self.out_test.shape)

    def build_model(self):
        self.model = Sequential()
        self.model.add(Dense(20, input_dim=8, activation='relu'))
        self.model.add(Dense(10, activation='relu'))
        self.model.add(Dense(10, activation='relu'))
        self.model.add(Dense(1, activation='linear'))
        self.model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    def train_model(self, epochs=1000):
        self.model.fit(self.inp_train, self.out_train, epochs=epochs, verbose=1)
        self.model.summary()

    def evaluate_model(self):
        output_pred = self.model.predict(self.inp_test)
        print('Coefficient of determination =', r2_score(self.out_test, output_pred))


if __name__ == "__main__":
    model = ConcreteModel('Concrete_data.xlsx')
    model.visualize_data()
    model.preprocess_data()
    model.split_data()
    model.build_model()
    model.train_model()
    model.evaluate_model()
