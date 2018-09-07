# Assignment:   Programming Quiz 3
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
What is the name for the bug in this code?
If there is no bug, write "no bug".

a = []
i = 1
while i > 0:
    a.append(i)
    i = i + 1
"""
# Answer:
"""
infinite while loop
"""


# Problem 2 (0.5 points)
"""
What is the highest numerical value that will be printed to the terminal?

a = [1, 2, 3, 4, 5]
for e in a:
    if e < len(a) - 1:
        print e
        continue
    break
"""
# Answer:
"""
3
"""


# Problem 3 (0.5 points)
"""
Both for loops and while loops can be converted into equivalent versions of one
another. However, in some cases, one is more convenient to use than the other.
Based on discussion from lecture, which one of the following statements is True?

Select one:
a. A while loop is more convenient when iterating over every element in a
   sequence in order.
b. A for loop is more convenient when an atypical stopping condition is
   required.
c. A for loop is more convenient when needing to index a sequence.
d. A for loop is more convenient when iterating over every element in a
   sequence in order.
"""
# Answer:
"""
C, D
"""

# Problem 4 (1.5 points)
#
# Write a function vowel_extractor that takes a single string argument. This
# function returns a list of the vowels that occur in the input string.
# Importantly, each such occurring vowel should only be output once; in other
# words, do not have duplicate vowels in the list returned.
#
# For this problem, the following letters are considered to always be vowels:
#   A, E, I, O, U, Y
#
# You may assume that the input will be an uppercase string but you should not
# make any assumptions about its length.

def vowel_extractor(someword):
    vowel_list = []
    if someword.find("A") >= 0:
        vowel_list.append("A")
    if someword.find("E") >= 0:
        vowel_list.append("E")
    if someword.find("I") >= 0:
        vowel_list.append("I")
    if someword.find("O") >= 0:
        vowel_list.append("O")
    if someword.find("U") >= 0:
        vowel_list.append("U")
    if someword.find("Y") >= 0:
        vowel_list.append("Y")
    return vowel_list
       

assert vowel_extractor("STRAWBERRY") == ["A", "E", "Y"]
assert vowel_extractor("BANANA") == ["A"]




# Problem 4 (2 points)
#
# Write a function firsts_only that takes a list of lists as an argument. This
# function returns a list that contains only the first element of each inner
# list within the outer list.
#
# You should not make any assumptions about the lengths of either the outer
# list or any of the inner lists.

def firsts_only(list_o_lists):
    firsts = []
    for i in range(len(list_o_lists)) :
        inside_lists = list_o_lists[i]
        firsts.append(inside_lists[0])
    return firsts

assert firsts_only([[1], [3]]) == [1, 3]
assert firsts_only([[1, 2, 3], [4, 5, 6]]) == [1, 4]




