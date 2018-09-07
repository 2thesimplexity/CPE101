# Assignment:   Programming Quiz 6
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Term:         Fall 2016
#
# The following programming quiz is worth 5 points.
# Please comment out any non-working code and test cases before submitting.
#
# IMPORTANT: You are prohibited from using any reference material - including 
#            code you have written in the past - during this quiz.


# Problem 1 (1.5 Points)
#
# Write a function to_pig_latin that takes 1 argument: word. This function
# returns its translation into Pig Latin, which has the following rules:
#
# 1. If the word begins with a vowel, simply return the word appended by "YAY".
# 2. If the word begins with a consonant, move ALL of the word's initial
#    consonants to the end of the word and append it with "AY".
# 
# See the test cases file funcs_tests for some examples. You may assume any 
# string passed to this function will be all upper case letters.
#
# Hint: Recall that "in" is a Boolean operator that tests for membership. 
#       For example:
#           ("A" in "AEIOU") evaluates to True
#           ("B" in "AEIOU") evaluates to False
#       Similarly, you can use "in" with the "not" Boolean operator:
#           ("A" not in "AEIOU") evalautes to False
#           ("B" not in "AEIOU") evaluates to True
#       You can test for membership as part of a condition for an if statement
#       or a while statement.
def to_pig_latin(word):
    if word[0] in 'AEIOU':
        translation = word + 'YAY'
    else:
        cons = ''
        for letter in word:
            if letter not in 'AEIOU':
                cons +=letter
            else:
                break
        translation = word[len(cons):] + cons + 'AY'
    return translation
assert to_pig_latin("INTEGER") == "INTEGERYAY"
assert to_pig_latin("BOOLEAN") == "OOLEANBAY"




# Problem 2 (2 Points)
#
# Write a function get_harmonic_mean that takes 1 argument: vals. This argument
# is a list of integers that MAY include zeros. The function must perform the
# following pattern operations in order:
#
#   1. Filter: Create a list f that contains all integers from vals EXCEPT any 
#              zeros.
#   2. Map:    Create a list m that has the reciprocal of all elements from f.
#              The reciprocals can be found by dividing 1 by each element in f
#              (e.g. the reciprocal of 4 is 1/4). Be sure NOT to do integer
#              division.
#   3. Reduce: Add up all the values from m and take the reciprocal of this 
#              sum. Multiply this sum by the number of elements in f (its
#              length). Return this product.
#
# Important: You may NOT use the filter, map, or reduce functions provided by
#            the Python language.

def get_harmonic_mean(vals):
    f = vals
    for val in vals:
        if val == 0:
            f.remove(0)
#    print f
    m = []
    for i in range(len(f)):
        m.append(1.0/float(f[i]))
    for i in range(len(m)):
        add_up = sum(m)
        recip = 1/add_up
        return round(recip*len(f), 2)

assert get_harmonic_mean([0]) == None
assert get_harmonic_mean([1]) == 1.0
assert get_harmonic_mean([0, 1, 0, 1, 0]) == 1.0
assert get_harmonic_mean([1, 2, 3, 4]) == 1.92
assert get_harmonic_mean([0, 2, 0, 4, 0, 6, 0, 8, 0]) == 3.84




# Problem 3 (1.5 Points)
#
# Write a function my_int that takes a string as input and returns an integer
# parsed from that string. However, if your function receives a string that
# does not consist soley of an integer value, it should handle the case
# gracefully (i.e. not throw an exception). Such cases should cause the
# function to behave in the following ways:
#
#   If the string contains a integer value, return that integer
#   If the string is empty, return "Empty String"
#   If the string contains characters, return "Character String"
#   If the string contains a float value (e.g. "3.14"), return "Float String"
#   If the string doesn't meet the above criteria, return "Unknown String"
#
# You must use try/except statement(s) to check for these cases.

def my_int(my_string):
    import string
    if my_string == '':
        return 'Empty String'
    if my_string.isdigit():
        return int(my_string)
    else:
        try:
            x = float(my_string)
            return 'Float String'
        except: 
            for char in my_string:
                if char in string.letters:
                    pass
                else:
                    return 'Unknown String'
            return 'Character String'
            
assert my_int("1") == 1
assert my_int("") == "Empty String"
assert my_int('ABcdEfG') == 'Character String'
assert my_int('ABc532') == 'Unknown String'
assert my_int('5.2226') == 'Float String'
assert my_int('5.2226a') == 'Unknown String'
