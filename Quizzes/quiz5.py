# Assignment:   Programming Quiz 5
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Term:         Fall 2016
#
# The following programming quiz is worth 5 points.
# Please comment out any non-working code and test cases before submitting.
#
# IMPORTANT: You are prohibited from using any reference material - including 
#            code you have written in the past - during this quiz.


#Read the class definition below to answer Problems 1 and 2.

#class Course:

# def __init__(self, dept, course, section):

#self.dept = dept
#self.course = course
#self.section = section

 #def __eq__(self, other):
 #    return self.course == other.course and self.section == other.section

 #c = Course("CPE", 101, 25)
# d = Course("CPE", 101, 25)




# Problem 1 (0.5 Points)
#
# Given the class definition and variable declarations above, what is the value
# of the following expression?
#
#   c == d
#
# Select one:
' a. True'
# a. False
# b. Objects cannot be compared




# Problem 2 (0.5 Points)
#
# Given the class definition and variable declarations above, what is the value
# of the following expression?
#
#   c != d
#
# Select one:
' a. True'
# a. False
# b. Objects cannot be compared




# Problem 3 (2.0 Points)
#
# Write a class Student that takes two arguments to its constructor:
# student_id (an integer) and final_grade (a single-character string).
#
# Two Student objects are considered equal if their IDs are the same.
# This class should have the following string representation:
#
#   "Student 1: A" (for an object with student_id 1 and final_grade "A")
#   "Student 2: C" (for an object with student_id 2 and final_grade "C")
#
# You must write __init__, __eq__, __ne__, and __repr__ functions (as discussed
# in lecture) as well as test cases for these operations.
#
# For simplicity, do not use +/- with letter grades.

class Student:

    def __init__(self,student_id,final_grade ):

        self.student_id = student_id
        self.final_grade= final_grade

    def __eq__(self, other):
        return self.student_id == other.student_id 

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return 'Student {0}: {1}'.format(self.student_id,self.final_grade)


# Examples (uncomment when class is implemented):
s1 = Student(1, "A")
s2 = Student(2, "B")
s3 = Student(3, "F")


# Problem 4 (2.0 Points)
#
# Write a function calculate_curve that takes as input a list of Student
# objects and returns an integer representing how many additional points should
# be added to each student's score. The target for this curve will be to make
# the average score in the class a B. Calculate the curve by subtracting the
# average of each student's final grade from the value of a B.
#
# This function should follow the convention for quantifying letter grades:
#       A: 4
#       B: 3
#       C: 2
#       D: 1
#       F: 0
#
# You may want to use the following built-in functions:
#   - sum       (to add all numbers in a list)
#   - len       (to get the length of a list)
#   - max       (to ensure the return value is not below 0)
#   - round     (to alter the precision)
#
# If the curve is less than 0 or the list is empty, this function should just
# return 0. Be sure that your answer does not extend beyond two decimal places.

def calculate_curve(student_list):
        
    grade_list = [student_list[i].final_grade for i in\
                     range(len(student_list))]
    
    num_list = []
    for i in range(len(grade_list)):    
        if grade_list[i] == 'A':
            num_list.append(4)    
        elif grade_list[i] == 'B':
            num_list.append(3)    
        elif grade_list[i] == 'C':
            num_list.append(2)    
        elif grade_list[i] == 'D':
            num_list.append(1)    
        elif grade_list[i] == 'F':
            num_list.append(0)    

    if len(grade_list) > 0:    
        average = sum(num_list)/float(len(num_list))
        average = round(average,2)
    else:
        return 0.0

    if 3 - average > 0:
        return 3 - average
    else:
        return 0.0



# Test Cases (uncomment when function is implemented):
assert calculate_curve([]) == 0.0
assert calculate_curve([Student(1, "B")]) == 0.0
assert calculate_curve([Student(1, "C")]) == 1.0
assert calculate_curve([Student(1, "A"), Student(2, "C")]) == 0.0
assert calculate_curve([Student(1, "A"), Student(2, "F")]) == 1.0
assert calculate_curve([Student(1, "B"), Student(2, "F")]) == 1.5
assert calculate_curve([Student(1, "D"), Student(2, "F")]) == 2.5
assert calculate_curve([Student(1, "A"),
                        Student(2, "C"), Student(3, "F")]) == 1.0
assert calculate_curve([Student(1, "C"),
                        Student(2, "D"), Student(3, "F")]) == 2.0
assert calculate_curve([Student(1, "A"),
                        Student(2, "D"), Student(3, "F")]) == 1.33


