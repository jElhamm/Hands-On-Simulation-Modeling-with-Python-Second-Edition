# *******************************************************************************************************
#                                                                                                       *
#                   Hands On Simulation Modeling with Python - Chapter 2                                *
#                                                                                                       *
#       This code defines a class RandomGenerator for generating various types of random                *
#       values using Python's random module. The RandomGenerator class includes methods for             *
#       generating random floating-point numbers (both with and without a seed), uniform                *
#       random floats within a range, random integers, values from a specified range, and               *
#       selecting random items from a list. It also includes a method for sampling data from a          *
#       list. In the main() function, an instance of RandomGenerator is created to generate and         *
#       display various random values in a formatted table. Additionally, it randomly selects           *
#       cities from a predefined list and samples data from a numeric range, printing the results.      *
#                                                                                                       *
# *******************************************************************************************************



import random
from tabulate import tabulate


class RandomGenerator:
    def __init__(self):
        self.seed_initialized = False

    def generate_random_float(self):
        return '{:05.4f}'.format(random.random())

    def generate_random_float_with_seed(self, seed):
        random.seed(seed)
        return '{:05.4f}'.format(random.random())

    def generate_uniform_random_float(self, min_val, max_val):
        return '{:6.4f}'.format(random.uniform(min_val, max_val))

    def generate_random_integer(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def generate_random_range(self, start, stop, step):
        return random.randrange(start, stop, step)

    def select_random_item(self, items_list):
        return random.choice(items_list)

    def sample_data(self, data_list, k):
        return random.sample(data_list, k)

def main():
    generator = RandomGenerator()
    # ------------------------------------------------- Generate values ----------------------------------------------------------

    random_floats = [generator.generate_random_float() for _ in range(20)]
    random_floats_seed = [generator.generate_random_float_with_seed(seed=1) for _ in range(20)]
    uniform_random_floats = [generator.generate_uniform_random_float(1, 100) for _ in range(20)]
    random_integers = [generator.generate_random_integer(-100, 100) for _ in range(20)]
    random_ranges = [generator.generate_random_range(0, 100, 5) for _ in range(20)]

    # ---------------------------------------------- Prepare data for table ------------------------------------------------------

    table_data = []
    for i in range(20):
        row = [
            f"{random_floats[i]:>10}",
            f"{random_floats_seed[i]:>10}",
            f"{uniform_random_floats[i]:>10}",
            f"{random_integers[i]:>10}",
            f"{random_ranges[i]:>10}"
        ]
        table_data.append(row)

    # ------------------------------------------------------ Print table ---------------------------------------------------------
        
    headers = ["Random Float", "Float with Seed", "Uniform Float", "Random Integer", "Random Range"]
    print("Generated Random Values:")
    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))

    # -------------------------------------------- Randomly select city from a list ----------------------------------------------

    cities_list = ['Rome', 'New York', 'London', 'Berlin', 'Moscow', 'Los Angeles', 'Paris', 'Madrid', 'Tokyo', 'Toronto']
    selected_cities = [generator.select_random_item(cities_list) for _ in range(10)]

    print("\nRandomly Selected Cities:")
    for city in selected_cities:
        print(f"Randomly selected item: {city}")

    # ----------------------------------------------- Sample data from a list ----------------------------------------------------
        
    data_list = range(10, 100, 10)
    data_sample = generator.sample_data(data_list, k=5)
    print("\nInitial Data List:")
    print(f"  {list(data_list)}")
    print(f"Sample Data List: {data_sample}")

if __name__ == "__main__":
    main()
