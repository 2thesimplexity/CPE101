# Name: Spencer Lawry     
# Name: Spencer Lawry     
	# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Lab Assignment: Characters and Filtering
# Term: Fall 2016        

def sum_101(my_list):
   mysum = 0
   for i in range(len(my_list)):
       mysum = my_list[i] + mysum
   return mysum

assert sum_101([1,5,3]) == 9
assert sum_101([-1,2,-1,5,5]) == 10
assert sum_101([-10,5,2,10,-30]) == -23

def index_of_smallest(my_list):
    if len(my_list) <= 0:
        return -1
    else:
        smallest = min(my_list)
        return my_list.index(smallest)

assert index_of_smallest([5,2,1,-5]) == 3
assert index_of_smallest([]) == -1
assert index_of_smallest([1,1,1,1,0]) == 4

def is_lower_101(char):
    return ord('a') <= ord(char) <= ord('z')


assert is_lower_101("a")  
assert not is_lower_101("A") 
assert is_lower_101("z")

def char_rot_13(char):
    if ord('a') <= ord(char) <= ord('m') or ord('A') <= ord(char) <= ord('M'):
        return chr(ord(char) + 13)
    if ord('n') <= ord(char) <= ord('z') or ord('N') <= ord(char) <= ord('Z'):
        return chr(ord(char) - 13)

assert char_rot_13('n') == 'a'
assert char_rot_13('m') == 'z'
assert char_rot_13('Z') == 'M'

def str_rot_13(my_str):
    rot_13_str = ''
    for i in range(len(my_str)):
        current_rot_char = char_rot_13(my_str[i])
        rot_13_str = rot_13_str + current_rot_char
    return rot_13_str

assert str_rot_13('apples') == 'nccyrf'   
assert str_rot_13('zigzag') == 'mvtmnt'
assert str_rot_13('AwEsOmE') == 'NjRfBzR'

def str_translate_101(my_str, old, new):
    str_translate = ''
    for i in range(len(my_str)):
        current_char = my_str[i]
        if current_char == old:
            current_char = new
        str_translate = str_translate + current_char
    return str_translate

assert str_translate_101('mississippi', 'i', 'z') == 'mzsszsszppz'
assert str_translate_101('lollipop', 'o', 'u') == 'lullipup'
assert str_translate_101('hippopotamus', 'p', 's') == 'hissosotamus'
        

















	
