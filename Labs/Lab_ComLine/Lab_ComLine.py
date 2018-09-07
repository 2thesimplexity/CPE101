# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Lab Assignment: Command Line Arguments
# Term: Fall 2016        

# Groups of 3 Function

def groups_of_3(vector):
    i = 0
    full_list = []
    sub_list = []
    for num in vector:
        i += 1
        if i <= 3:
            sub_list.append(num)
        else:
            full_list.append(sub_list)
            sub_list = []
            sub_list.append(num)
            i = 1 
    return full_list + [sub_list]

assert groups_of_3([1,2,3,4,5,6]) == [[1,2,3],[4,5,6]]
assert groups_of_3([1,2,3,4,5,6,7]) == [[1,2,3],[4,5,6],[7]]
assert groups_of_3([1,2,3,4,5,6,7,8]) == [[1,2,3],[4,5,6],[7,8]]

# File Input, Command Line Arguements, Try/Except

import sys
def com_line():
    arg_list = sys.argv
    if len(arg_list) > 3 or len(arg_list) < 2 or\
       len(arg_list) == 3 and '-s' not in arg_list:

        print 'Usage: [-s] file_name'

    else:

        if '-s' in arg_list:
            sum_up = True
            arg_list.remove('-s')
        else:
            sum_up = False

        try: 
            f = open(arg_list[1], 'r')

            int_count = 0
            float_count = 0
            other_count = 0
            sum_count = 0

            while True:
                line = f.readline()
                if line == '':
                    break
                line_list = line.split()

                for thing in line_list:
                    if thing.isdigit(): 
                        thing = int(thing)
                        int_count += 1
                        if sum_up:
                            sum_count += thing
                    else:
                        try: 
                            thing = float(thing)
                            float_count += 1
                            if sum_up:
                                sum_count += thing
                        except: 
                            other_count += 1
            f.close()

            fmt_str = 'Ints: {0}\nFloats: {1}\nOther: {2}'
            print fmt_str.format(int_count, float_count, other_count)
            if sum_up:
                print 'Sum: {0}'.format(sum_count)

        except:
            print 'Unable to open {0}'.format(arg_list[1])

com_line()
