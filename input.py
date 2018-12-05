from course import Course
from teacher import Teacher


def get_input():
    d, t = map(int, raw_input().split())

    c = input()
    happiness_courses = []
    happiness_courses = map(int, raw_input().split())
    courses = []
    for i in range(c):
        course = Course(happiness_courses[i], i+1)
        courses.append(course)

    teachers = []
    p = input()
    for i in range(p):
        courses_presented = map(int, raw_input().split())
        del courses_presented[0]
        temp_c = []
        teacher = Teacher(i+1)
        for j in range(len(courses_presented)):
            temp_c.append(courses[courses_presented[j]-1])
            courses[courses_presented[j]-1].set_teacher(teacher)
        teacher.set_courses(temp_c)
        teachers.append(teacher)

    sadness = []
    for i in range(c):
        sadnessFirstDimension = list(map(int, raw_input().split()))
        sadness.append(sadnessFirstDimension)
    
    return d, t, courses, teachers, sadness
