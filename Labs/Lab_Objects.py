# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Lab Assignment: Polynomials and Patterns
# Term: Fall 2016        

# Objects
    
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __ne__(self,other):
        return not self == other
point1_copy = Point(1,2)
point1 = Point(1,2) 
point2 = Point(-1,5)
point3 = Point(0,0)
assert point1.y == 2 
assert point2.x == -1
assert point3.x == 0
assert point1 == point1_copy
assert point1 != point2
assert point1 != point3

class Circle:
    def __init__(self,point,radius):
        self.point = point
        self.radius = radius

circle1 = Circle(point1, 2)
circle2 = Circle(point2, 4)
circle3 = Circle(point3, 6)
assert circle1.point == point1
assert circle2.radius == 4
assert circle3.radius == 6

# Functions on Point and Circle

def distance(p1,p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5  

assert distance(point1,point2) == ((13)**0.5)
assert distance(point2,point1) == ((13)**0.5)
assert distance(point2,point3) == ((26)**0.5)

def circles_overlap(circle1,circle2):
    return (circle1.radius + circle2.radius) > distance(circle1.point, \
                                                        circle2.point)

assert circles_overlap(circle1,circle2) 
assert circles_overlap(circle2,circle1)
assert circles_overlap(circle2,circle3)

# List Comprehensions and Objects

def distance_all(points):
    distance_all = [distance(Point(0,0),point) for point in points]
#    dist_list = []
#    for point in points:
#        dist = distance(Point(0,0),point)
#        dist_list.append(dist)
#    return dist_list
    return distance_all

assert distance_all([point1,point2]) == [(5)**0.5, (26)**0.5]
assert distance_all([point2,point1]) == [(26)**0.5, (5)**0.5]
assert distance_all([point2,point3]) == [(26)**0.5, 0]
 
def are_in_first_quadrant(points):
    return [point for point in points if point.x > 0 and point.y > 0]

assert are_in_first_quadrant([point1,point2,point3]) == [point1]
assert are_in_first_quadrant([point2,point3]) == []
assert are_in_first_quadrant([point1,point1,point2]) == [point1,point1]


# File Input    

def print_file(file_name):
    f = open(file_name, 'r')
    i = 0
    while True:
        line = f.readline().strip()
        if line == '':
            break
        print 'Line {0:d} ({1:d} chars): {2}'.format(i,len(line),line) 
        i += 1
    f.close()

print_file('in.txt') 


