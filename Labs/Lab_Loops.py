# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Lab Assignment: Conditions and Loops 
# Term: Fall 2016        

def max_101(x,y):
    if x > y: 
	return x
    elif y >= x:
        return y

assert max_101(5,10) == 10
assert max_101(5,-10) == 5
assert max_101(-1,-1) == -1

def max_of_three(x,y,z):
   if x > y and x > z :
	return x
   elif y > z : 
        return y
   else:
        return z
        

assert max_of_three(10,10,10) == 10
assert max_of_three(-10,3.0,3.0) == 3.0
assert max_of_three(10.5,10.5,5) == 10.5


def repeated_max_of_three():
    while 2 == 2: 
	a = raw_input("Number One!(enter q to escape at any time) ")
        if a == "q":
            break
	b = raw_input("Number Two! ")
        if b == "q":
            break
	c = raw_input("Number Three! ")
        if c == "q":
            break
        print max_of_three(a,b,c)
