

class Teacher:
    def __init__(self, teacher_number):
        self.courses = []
        self.teacher_number = teacher_number


    def get_courses(self):
        return self.courses


    def set_courses(self, courses):
        self.courses = courses

    
    def get_teacher_number(self):
        return self.teacher_number


    def get_courses_numbers(self):
        result = []
        for i in self.courses:
            result.append(i.get_cnumber())
        return result