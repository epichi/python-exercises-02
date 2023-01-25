import sys 

numbers = [int(sys.argv[i]) for i in range(1, len(sys.argv))]

def max_value(list):
    # set first element as max
    max = list[0]
    for i in list:
        # check if the current element is greater than max
        if i > max:
            max = i
    return max

def min_value(list):
    # set first element as min
    min = list[0]
    for i in list:
        # check if the current element is smaller than min
        if i < min:
            min = i
    return min

max_value = max_value(numbers)
min_value = min_value(numbers)
max_index = numbers.index(max_value)
min_index = numbers.index(min_value)
    
print(f'The min is {min_value} and its position is {min_index}')   
print(f'The max is {max_value} and its position is {max_index}')
