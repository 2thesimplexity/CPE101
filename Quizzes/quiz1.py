# Assignment:   Programming Quiz 1
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Term:         Fall 2016
#
# The following programming quiz is worth 5 points.
# Please comment out any non-working code and test cases before submitting.
#
# IMPORTANT: You are prohibited from using any reference material - including 
#            code you have written in the past - during this quiz.

import math


# Multiple Choice 1 (0.5 points)
"""
Over which of the following intervals for x is this expression satisfied
(made to be True)?

x <= 0 and x >= 0

Select one:
a. [0, 0]
b. (-inf, 0], [0, inf)
c. (-inf, inf)
d. Not satisfiable
e. (-inf, 0), (0, inf)
"""
# Answer:
"""
A
"""


# Multiple Choice 2 (0.5 points)
"""
What is the most likely cause of the following error?

File "test.py", line 7
if x = y:
     ^
SyntaxError: invalid syntax

Select one:
a. The variable y was not initialized.
b. Both variables x and y were not initialized.
c. The assignment operator is being used instead of the equality operator.
d. The conditional test should be in parenthesis.
e. The variable x was not initialized.
"""
# Answer:
"""
C
"""


# Multiple Choice 3 (0.5 points)
"""
What is the most likely cause of the following error?

File "test.py", line 3
return print x, y
           ^
SyntaxError: invalid syntax

Select one:
a. Both the variables x and y were not initialized.
b. The variable x was not initialized.
c. The concatenation operator should be used instead of the comma operator.
d. The variables x and y should be surrounded by quotation marks.
e. Print statements are not expressions and thus cannot be returned.
"""
# Answer:
"""
E
"""


# Programming Problem 1 (1.5 points)
#
# Write a function find_discriminant that takes 3 arguments: a, b, c. This
# function returns the result of calculating the discriminant as part of the
# quadratic formula (see the board).
#
# If the discriminant is less than 0, return None.


def find_discriminant(a, b, c):
   disc =  b**2 - (4*a*c)
   if disc >= 0:
      return disc
   else:
      return None



assert find_discriminant(0, 5, 0) == 25
assert find_discriminant(1, 0, 1) is None
assert find_discriminant(1, 1, 1) is None


# Programming Problem 2 (2 points)
#
# Write a function solve_poly that takes 3 arguments: a, b, c. This function
# returns the result of computing the quadratic formula for ONE value of x 
# (see the board).
#
# You MUST use your previous function, find_discriminant, in your 
# implementation. Again, if the discriminant is less than 0, solve_poly must 
# return None. As this is not a math course, test cases have been provided.

def solve_poly(a, b, c):
   if find_discriminant(a, b, c) == None:
      return None
   else:
      return (-b + math.sqrt(find_discriminant(a, b, c)))/(2*a)





assert solve_poly(1, 0, 1) is None
assert solve_poly(1, 1, 1) is None
assert solve_poly(1, 1, 0) == 0
assert solve_poly(1, -2, 1) == 1
assert solve_poly(1, 2, 1) == -1


