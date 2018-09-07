# Assignment:   Programming Quiz 4
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Term:         Fall 2016
#
# The following programming quiz is worth 5 points.
# Please comment out any non-working code and test cases before submitting.
#
# IMPORTANT: You are prohibited from using any reference material - including 
#            code you have written in the past - during this quiz.


# Problem 1 (0.5 points)
"""
Using the find or index function, what would go into the blank (underlined
section) below to perform a slice on the given variable to print out "California".

    school = "Cal Poly"
    print school[0:3] + "ifornia"


"""
# Answer:
"""
0:3
"""


# Problem 2 (0.5 points)
"""
Which of the following while loops is equivalent to the for loop below?

a = [1, 2, 3]

for e in a:
    print e

Select one:
a.  a = [1, 2, 3]
    i = 0
    while i < len(a):
        print a[i]
        i = i + 1

b.  a = [1, 2, 3]
    i = 1
    while i < len(a) - 1:
        print a[i]
        i = i + 1

c.  a = [1, 2, 3]
    i = 1
    while i < len(a):
        print a[i]
        i = i + 1

d.  a = [1, 2, 3]
    i = 0
    while i < len(a) - 1:
        print a[i]
        i = i + 1
"""
# Answer:
"""
A
"""


# Problem 3 (2 points)
#
# Write a function multi_list that takes a list of integers as input and
# returns a list of lists such that each inner list repeats the corresponding
# integer in the original list that number of times.
#
# If the input list is empty, this function should return an empty list. If any
# integers in the input list are non-positive, that integer should not have a
# corresponding inner list.
#
# See the provided test cases below for examples. These cases are exhaustive.
# Extra 0.5 credit awarded for a list comprehension implementation.

def multi_list(input_list):
    list_o_lists = []
    for i in range(len(input_list)):
        if input_list[i] >= 0:
            mult = input_list[i]
        else: mult = 0 
        square_list = [input_list[i]]*mult
        if square_list == []:
            continue
        list_o_lists.append(square_list)
    return list_o_lists


assert multi_list([]) == []
assert multi_list([1]) == [[1]]
assert multi_list([1, 2, 3, 4]) == [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]
assert multi_list([-1]) == []
assert multi_list([1, 2, 0, -1, 3]) == [[1], [2, 2], [3, 3, 3]]


# Problem 4 (2 points)
#
# Write a function running_total that takes a list of numbers and returns the
# cumulative sum; that is, a new list where the ith element is the sum of the
# first i + 1 elements from the original list.
#
# See the provided test cases below for examples. These cases are exhaustive.
# Extra 0.5 credit awarded for a list comprehension implementation.

def running_total(input_list):
    sum_list = []
    current_sum = 0
    for i in range(len(input_list)):
        current_value = input_list[i]
        current_sum = current_value + current_sum
        sum_list.append(current_sum)
    return sum_list

assert running_total([]) == []
assert running_total([1]) == [1]
assert running_total([1, 2]) == [1, 3]
assert running_total([1, 2, 3]) == [1, 3, 6]
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]


