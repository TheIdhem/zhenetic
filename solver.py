from program import Program
import random
import math
MUTATION_PROBABILITY = 0.01
CHILDREN_SELECTION = 0.8


class Solver:
    def __init__(self, d, t, courses, teachers, sadness, population_size):
        self.population_size = population_size
        self.d = d
        self.t = t
        self.courses = courses
        self.teachers = teachers
        self.population = []
        self.sadness = sadness
        self.best_result_number = 0
        self.best_result = []
        self.iteration = 0



    def find_course(self, courses_number):
        for i in range(len(self.courses)):
            if self.courses[i].get_cnumber() == courses_number:
                return self.courses[i]
        #throm exception


    def run(self):
        self.start_info()
        self.initiate_population()
        self.genetic()
        # self.print_output()


    def initiate_population(self):
        for i in range(self.population_size):
            chromosome = Program(self.courses, self.teachers, (self.d*self.t))
            chromosome.init_gen()
            self.population.append(chromosome.get_slots())


    def fitness_function(self, chromosome):
        result = 0
        for i in range(len(chromosome)):
            for key, value in chromosome[i].iteritems():
                result += self.find_course(key).get_happines()
        minus = 0
        for i in range(len(chromosome)):
            for key1, value1 in chromosome[i].iteritems():
                for key2, value2 in chromosome[i].iteritems():
                    minus += self.sadness[key1-1][key2-1]
        minus /= 2
        result -= minus
        return result


    def save_best(self):
        for i in range(len(self.population)):
            self.population[i] = self.check_gen(self.population[i])
            result = self.fitness_function(self.population[i])
            if result > self.best_result_number:
                self.iteration = 0
                print "Better result:", result
                self.best_result_number = result
                self.best_result = self.population[i]
                for i in range(len(self.best_result)):
                    for key, value in self.best_result[i].iteritems():
                        print "     Course number:", key, "Teacher number:", value.get_teacher_number(),
                        print "Day:", int(i/self.t), "Time:", int(i % self.t)
                print "\n"


    def genetic(self):

        for j in range(len(self.population)):
            self.population[j] = self.check_gen(self.population[j])

        new_population = []
        iteration_number = 0
        while self.iteration != 1000:
            self.save_best()
            for i in range(len(self.population)):

                parents = self.select_parents()
                chromosome = self.crossover(parents)
                chromosome = self.mutation(chromosome)
                chromosome = self.check_gen(chromosome)
                chromosome = self.mutation2(chromosome)
                chromosome = self.check_gen(chromosome)
                new_population.append(chromosome)

            new_population = random.sample(new_population, int(len(new_population)* CHILDREN_SELECTION)) + self.best()
            self.population = new_population
            new_population = []
            iteration_number += 1
            self.iteration += 1
            print "Iteraion#:", iteration_number


    def check_gen(self, chromosome):
        thought_course = [False] * len(self.courses)
        for j in range(len(chromosome)):
            for k in chromosome[j].keys():
                if thought_course[k-1]:
                    del chromosome[j][k]
                else:
                    thought_course[k-1] = True
        return chromosome


    def mutation2(self, chromosome):
        not_thought_course = []
        for i in range(len(self.courses)):
            not_thought_course.append(i+1)
        for j in range(len(chromosome)):
            for k in chromosome[j].keys():
                not_thought_course.remove(k)
        for i in range(len(not_thought_course)):
            if self.courses[not_thought_course[i]-1].has_teacher():
                teacher = self.courses[not_thought_course[i]-1].get_random_teacher()
                slot = random.randint(0, len(chromosome)-1)
                if teacher not in chromosome[slot].values():
                    chromosome[slot][not_thought_course[i]] = teacher
        return chromosome
            



    def best(self):
        last_index = math.ceil(len(self.population)*(1-CHILDREN_SELECTION))
        return sorted(self.population, key=lambda x: self.fitness_function(x))[len(self.population)-int(last_index):]


    def mutation(self, chromosome):
        if random.random() <= MUTATION_PROBABILITY:
            index = random.randint(0, len(chromosome)-1)
            index2 = random.randint(0, len(chromosome)-1)
            temp = chromosome[index]
            chromosome[index] = chromosome[index2]
            chromosome[index2] = temp
        return chromosome




    def crossover(self, parents):
        if len(parents[0]) < 4:
            middle = random.randint(0, len(parents[0])-1)
        else:
            middle = random.randint(2, len(parents[0])-2)
        return parents[0][:middle] + parents[1][middle:]


    def select_parents(self):
        return random.sample(self.population, 2)



    def start_info(self):
        print "Starting..."
        print "     Population size:", self.population_size, ""
        print "     CHILDREN_SELECTION:", CHILDREN_SELECTION, "\n"


    # def print_output(self):
    #     print "Output:"
    #     print self.best_result_number
    #     for i in range(len(self.best_result)):
    #         for key, value in self.best_result[i].iteritems():
    #             print "     Course number:", key, "Teacher number:", value.get_teacher_number(),
    #             print "Day:", int(i/self.t), "Time:", int(i%self.t)

    #     print "End."
