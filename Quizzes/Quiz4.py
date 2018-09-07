# this is a test

test_list = [5, 5, 3, 5, 2]

def remove_duplicates(test_list):
#    unique_list = []
#    for i in range(len(test_list)):
#        if test_list[i] not in unique_list:
#            unique_list.append(test_list[i])
#    return unique_list
    unique_list = set(test_list)
    return unique_list
print remove_duplicates(test_list)

def multi_list(input_list):
    square_list = []
    for i in range(len(input_list)):
        new_list = [input_list[i]]*input_list[i]
        square_list.append(new_list)
    return square_list

