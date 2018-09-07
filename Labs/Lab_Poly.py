# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Lab Assignment: Polynomials and Patterns
# Term: Fall 2016        

def poly_add2(poly1, poly2):
    poly_new = []
    poly_new.append (poly1[0] + poly2[0])
    poly_new.append (poly1[1] + poly2[1]) 
    poly_new.append (poly1[2] + poly2[2]) 
    return poly_new

assert poly_add2([5, 2, 3], [2, 3, 5]) == [7, 5, 8]
assert poly_add2([1, -2, 5], [-1, 0, 2]) == [0, -2, 7]
assert poly_add2([3, 4, 6], [-5, 10, 3]) == [-2, 14, 9]

