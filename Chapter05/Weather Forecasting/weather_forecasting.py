import numpy as np
import matplotlib.pyplot as plt

class WeatherForecast:
    def __init__(self, num_days=365):
        self.num_days = num_days
        self.states_data = ["Sunny", "Rainy"]
        self.transition_states = [["SuSu", "SuRa"], ["RaRa", "RaSu"]]
        self.transition_matrix = [[0.80, 0.20], [0.25, 0.75]]
        self.weather_forecasting = []
        np.random.seed(3)

    def predict_weather(self):
        today_prediction = self.states_data[0]
        print("Weather initial condition =", today_prediction)

        for i in range(1, self.num_days):
            if today_prediction == "Sunny":
                trans_condition = np.random.choice(
                    self.transition_states[0], replace=True, p=self.transition_matrix[0]
                )
                if trans_condition == "SuSu":
                    pass
                else:
                    today_prediction = "Rainy"
            elif today_prediction == "Rainy":
                trans_condition = np.random.choice(
                    self.transition_states[1], replace=True, p=self.transition_matrix[1]
                )
                if trans_condition == "RaRa":
                    pass
                else:
                    today_prediction = "Sunny"

            self.weather_forecasting.append(today_prediction)
            print(today_prediction)

    def plot_weather(self):
        plt.plot(self.weather_forecasting)
        plt.show()

        plt.figure()
        plt.hist(self.weather_forecasting)
        plt.show()


def main():
    weather_model = WeatherForecast(num_days=365)
    weather_model.predict_weather()
    weather_model.plot_weather()

if __name__ == "__main__":
    main()