import random
from function import *

#class Chromosome
class Program:
    def __init__(self, courses, teachers, gen_number):
        self.courses = courses
        self.teachers = teachers
        self.gen_number = gen_number
        self.slot = []
        for i in range(gen_number):
            temp = {}
            self.slot.append(temp)


    def get_slots(self):
        return self.slot


    # def init_gen(self):
    #     thought_course = [False] * len(self.courses)
    #     temp_teachers = mix_array(self.teachers)
    #     for i in range(len(temp_teachers)):
    #         teacher_courses = temp_teachers[i].get_courses_numbers()
    #         for j in range(self.gen_number):
                # if len(teacher_courses) == 0:
                #     break
    #             # print len(teacher_courses)
    #             num = random.randint(0, len(teacher_courses)-1)
    #             if thought_course[teacher_courses[num]-1] == False:
    #                 self.slot[j][teacher_courses[num]] = temp_teachers[i]
    #                 thought_course[teacher_courses[num]-1] = True
    #             del teacher_courses[num]


    def init_gen(self):
        temp_teachers = mix_array(self.teachers)
        for i in range(len(temp_teachers)):
            teacher_courses = temp_teachers[i].get_courses_numbers()
            for j in range(self.gen_number):
                if len(teacher_courses) == 0:
                    break
                num = random.randint(0, self.gen_number-1)
                num2 = random.randint(0, len(teacher_courses)-1)
                self.slot[num][teacher_courses[num2]] = temp_teachers[i]
                del teacher_courses[num2]
