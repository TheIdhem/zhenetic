from input import *
from solver import Solver

POPULATION_SIZE = 15


if __name__ == '__main__':
    d, t, courses, teachers, sadness = get_input()

    solver = Solver(d, t, courses, teachers, sadness, POPULATION_SIZE)
    solver.run()
