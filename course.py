import random

class Course:
    def __init__(self, happines, number):
        self.happines = happines
        self.number = number
        self.teachers = []

    def get_cnumber(self):
        return self.number
        

    def get_happines(self):
        return self.happines


    def set_teacher(self, teacher):
        self.teachers.append(teacher)


    def has_teacher(self):
        if len(self.teachers) > 0:
            return True
        return False

    def get_random_teacher(self):
        number = random.randint(0, len(self.teachers)-1)
        return self.teachers[number]