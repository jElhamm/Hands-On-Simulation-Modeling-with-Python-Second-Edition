import numpy as np


class GeneticAlgorithm:
    def __init__(self, var_values, num_coeff=4, pop_chrom=10, sel_rate=5, num_gen=100):
        self.var_values = np.array(var_values)
        self.num_coeff = num_coeff
        self.pop_chrom = pop_chrom
        self.sel_rate = sel_rate
        self.num_gen = num_gen
        self.pop_size = (pop_chrom, num_coeff)
        self.population = np.random.uniform(low=-10.0, high=10.0, size=self.pop_size)
        print("Initial population:\n", self.population)

    def calculate_fitness(self):
        return np.sum(self.population * self.var_values, axis=1)

    def select_parents(self, fitness):
        parents = np.empty((self.sel_rate, self.num_coeff))
        for i in range(self.sel_rate):
            max_fitness_idx = np.argmax(fitness)
            parents[i, :] = self.population[max_fitness_idx, :]
            fitness[max_fitness_idx] = np.min(fitness)
        return parents

    def crossover(self, parents):
        offspring_size = (self.pop_chrom - self.sel_rate, self.num_coeff)
        offspring = np.empty(offspring_size)
        crossover_point = offspring_size[1] // 2

        for j in range(offspring_size[0]):
            parent1_idx = np.random.randint(0, parents.shape[0])
            parent2_idx = np.random.randint(0, parents.shape[0])
            offspring[j, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
            offspring[j, crossover_point:] = parents[parent2_idx, crossover_point:]

        return offspring

    def mutate(self, offspring):
        for m in range(offspring.shape[0]):
            mutation_value = np.random.uniform(-1.0, 1.0)
            mutation_index = np.random.randint(0, offspring.shape[1])
            offspring[m, mutation_index] += mutation_value
        return offspring

    def optimize(self):
        for gen in range(self.num_gen):
            fitness = self.calculate_fitness()
            print(f"Generation {gen}: Best fitness value = {np.max(fitness)}")
            parents = self.select_parents(fitness.copy())
            offspring = self.crossover(parents)
            offspring = self.mutate(offspring)
            self.population[:self.sel_rate, :] = parents
            self.population[self.sel_rate:, :] = offspring

        final_fitness = self.calculate_fitness()
        best_idx = np.argmax(final_fitness)
        print("Optimized coefficient values:", self.population[best_idx, :])
        print("Maximum value of y:", final_fitness[best_idx])


def main():
	var_values = [1, -3, 4.5, 2]
	ga = GeneticAlgorithm(var_values=var_values, num_coeff=4, pop_chrom=10, sel_rate=5, num_gen=100)
	ga.optimize()


if __name__ == "__main__":
    main()