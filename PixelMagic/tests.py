# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Pixel Magic 
# Term: Fall 2016        

import pixel_magic

#groups_of_3 tests

assert pixel_magic.groups_of_3([1,2,3,4,5,6]) == [[1,2,3],[4,5,6]] 
assert pixel_magic.groups_of_3([1,2,3,4,5,6,7]) == [[1,2,3],[4,5,6],[7]]                  
assert pixel_magic.groups_of_3([1,2,3,4,5,6,7,8]) == [[1,2,3],[4,5,6],[7,8]]  

# decode_puzzle tests

test1 = pixel_magic.groups_of_3(range(9))
test2 = pixel_magic.groups_of_3([5]*9)
test3 = pixel_magic.groups_of_3([10,100,1000,10000,100000,1000000])

assert pixel_magic.decode_puzzle(test1) == [[0,0,0],[30,30,30],[60,60,60]]
assert pixel_magic.decode_puzzle(test2) == [[50,50,50],[50,50,50],[50,50,50]]
assert pixel_magic.decode_puzzle(test3) == [[100,100,100],[255,255,255]]

# fade_image tests

fade1 = pixel_magic.groups_of_3(range(27))
fade1_header  = [3,3,255]

assert pixel_magic.fade_image(fade1, 1, 1, 1, fade1_header)\
       == [[0,0,0], [0,0,1], [1,1,1],\
           [1,2,2], [12,13,14], [3,3,3],\
           [3,3,4], [4,4,4], [4,5,5]]

fade2 = pixel_magic.groups_of_3(range(36))
fade2_header = [3,4,255]

assert pixel_magic.fade_image(fade2, 1, 1, 1, fade2_header)\
       == [[0,0,0], [0,0,1], [1,1,1],\
           [1,2,2], [12,13,14], [3,3,3],\
           [3,3,4], [4,4,4], [4,5,5],\
           [5,5,5], [6,6,6], [6,6,7]]

fade3 = pixel_magic.groups_of_3([0]*27)
fade3_header = [3,3,255]

assert pixel_magic.fade_image(fade3, 1, 1, 1, fade3_header)\
       == [[0,0,0]]*9
