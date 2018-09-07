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


# Problem 1 (0.5 points)
"""
Over which of the following intervals for x is this expression satisfied
(made to be True)?

    x >= 3 and x < 1 or x >= 2 and x < 3

Select one:
a. (-inf, 1)
b. [2, 3)
c. [2, 2]
d. (-inf, 1), [2, 3)
e. Not satisfiable
"""
# Answer:
"""
B
"""


# Problem 2 (0.5 points)
"""
is_integer is a function that takes an integer, float, or string as input and
returns True if the value is of type integer.

For example, 1 is an integer but 1.0 is not.

Which of the following sets of values represent its best edge cases?

Select one:
a. 0, 1, 1.0
b. 0.0, 1.0, "1"
c. 0, 1.0, "1"
d. 0, 1, "1"
"""
# Answer:
"""
C
"""


# Problem 3 (0.5 points)
"""
The following function takes two arguments and intends to return a^b.

On what numbered line(s) does this code have a syntactic or logical bug?
Write all lines of code that have a bug (comma-separated).

1. def f(a, b)
2.     if b == 0:
3.         return 1
4.     else
5.         return a * b
"""
# Answer:
"""
1,4,5 
"""


# Problem 4 (0.5 points)
"""
The following function takes the values of two sides of a right triangle and
returns the value of the triangle's hypotenuse. 

On what numbered line(s) does this code have a syntactic or logical bug?
Write all lines of code that have a bug (comma-separated).

1. def hypotenuse(a, b)
2.     x = a ** 2
3.     y = b ** 2
4.     c = sqrt(x + y)
5.     print c
"""
# Answer:
"""
1,4,5
"""

# Problem 5 (3 points)
#
# Write a function sum_nums that takes 3 arguments: start, stop, step. This
# function returns the sum of a range of integers that begin at start, end just
# before stop, and increment by step for each subsequent integer.
#
# For example, if start is 4, stop is 10, and step is 2, then the sum of this
# range of integers would be 4 + 6 + 8 = 18. If start is 2, stop is 11, and
# step is 3, then the range would be 2 + 5 + 8 = 15.
#
# You may assume that start and stop will be non-negative integers and that 
# step will be a positive integer.




def sum_nums(start, stop, step):
    value = start
    sum_values = 0  
    while value < stop:
       sum_values = sum_values + value
       value = value + step
    return sum_values 



assert sum_nums(4, 10, 2) == 18
assert sum_nums(2, 11, 3) == 15


