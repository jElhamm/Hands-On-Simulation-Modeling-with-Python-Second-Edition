import numpy as np
import matplotlib.pyplot as plt


class CellularAutomaton:
    def __init__(self, cols_num=100, rows_num=100, wolfram_rule=126):
        self.cols_num = cols_num
        self.rows_num = rows_num
        self.wolfram_rule = wolfram_rule
        self.cell_state = np.zeros((rows_num, cols_num), dtype=np.int8)
        self.update_window = np.array([[4], [2], [1]])
        self.bin_rule = self._get_binary_rule()
        self.initialize_first_row()

    def _get_binary_rule(self):
        bin_rule = np.array([int(bit) for bit in np.binary_repr(self.wolfram_rule, 8)])
        print('Binary rule is:', bin_rule)
        return bin_rule

    def initialize_first_row(self):
        self.cell_state[0, :] = np.random.randint(0, 2, self.cols_num)

    def generate_automaton(self):
        for j in range(self.rows_num - 1):
            update = np.vstack((np.roll(self.cell_state[j, :], 1), 
                                self.cell_state[j, :], 
                                np.roll(self.cell_state[j, :], -1))).astype(np.int8)
            rule_up = np.sum(update * self.update_window, axis=0).astype(np.int8)
            self.cell_state[j + 1, :] = self.bin_rule[7 - rule_up]

    def display(self):
        plt.imshow(self.cell_state, cmap=plt.cm.binary)
        plt.show()


def main():
	automaton = CellularAutomaton(cols_num=100, rows_num=100, wolfram_rule=126)
	automaton.generate_automaton()
	automaton.display()


if __name__ == "__main__":
    main()