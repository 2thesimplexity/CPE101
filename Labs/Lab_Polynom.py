# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Lab Assignment: Polynomials & Patterns 
# Term: Fall 2016        

# POLYNOMIALS

def poly_add2(poly1, poly2):
    poly_add2 =[poly1[0]+poly2[0], poly1[1]+poly2[1],+poly1[2]+poly2[2]]
    return poly_add2

assert poly_add2([1,2,3],[3,2,1]) == [4,4,4]
assert poly_add2([-1,0,3],[1,0,-3]) == [0,0,0]
assert poly_add2([3,3,3],[1,1,1]) == [4,4,4]

def poly_mult2(poly1,poly2):
    poly_mult2 = []
    poly_mult2.append (poly1[0]*poly2[0])
    poly_mult2.append (poly1[0]*poly2[1]+poly1[1]*poly2[0])
    poly_mult2.append (poly1[0]*poly2[2]+poly1[1]*poly2[1]+poly1[2]*poly2[0])
    poly_mult2.append (poly1[1]*poly2[2]+poly1[2]*poly2[1])
    poly_mult2.append (poly1[2]*poly2[2])
    return poly_mult2

assert poly_mult2([1,2,3],[3,2,1]) == [3,8,14,8,3]
assert poly_mult2([-1,0,3],[1,0,-3]) == [-1,0,6,0,-9] 
assert poly_mult2([3,3,3],[1,1,1]) == [3,6,9,6,3]

# MAP PATTERN

def square_all(num_list):
    square = [num**2 for num in num_list]
    return square

assert square_all([1,2,3,4,5]) == [1,4,9,16,25]
assert square_all([3,7,3]) == [9,49,9]
assert square_all([0,-1,-3,-5,-9]) == [0,1,9,25,81]

def add_n_all(number,num_list):
    for i in range(len(num_list)):
        num_list[i] = num_list[i]+number
    return num_list

assert add_n_all(5,[1,2,3]) == [6,7,8]
assert add_n_all(-2,[0,0,0]) == [-2,-2,-2]
assert add_n_all(0,[1,2,3]) == [1,2,3]

def even_or_odd_all(int_list):
    i = 0
    while i < len(int_list):
        int_list[i] = (int_list[i] % 2 == 0)
        i+= 1
    return int_list

assert even_or_odd_all([1,5,2,6,3]) == [False,False,True,True,False]
assert even_or_odd_all([5,3,1,-1]) == [False,False,False,False]
assert even_or_odd_all([2,4,8,6,12]) == [True,True,True,True,True]

# FILTER PATTERN

def are_positive(num_list):
    positives = [num_list[i] for i in range(len(num_list)) if num_list[i] > 0]
    return positives

assert are_positive([1,5,-2,3,-1]) == [1,5,3]
assert are_positive([-5,10,-1,0,1]) == [10,1]
assert are_positive([-1,-2,-3,-4]) == [] 

def are_greater_than_n(number,num_list):
    great_list = []
    for i in range(len(num_list)):
        if num_list[i] > number:
            great_list.append(num_list[i])
    return great_list

assert are_greater_than_n(3,[1,5,2,10]) == [5,10]
assert are_greater_than_n(-1,[1,5,2,10]) == [1,5,2,10]
assert are_greater_than_n(10,[1,5,2,10]) == []

def are_divisible_by_n(number,int_list):
    i = 0
    div_list = []
    while i < len(int_list):
        if int_list[i] % number == 0:
            div_list.append(int_list[i])
        i += 1
    return div_list

assert are_divisible_by_n(5,[10,2,3,15]) == [10,15]
assert are_divisible_by_n(2,[4,8,3,2]) == [4,8,2]
assert are_divisible_by_n(10,[100,5,-10]) == [100,-10]

