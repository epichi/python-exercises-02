import sys

args_length = len(sys.argv)
if args_length == 1:
    print('Error! No string given')
else:
    input_string = str(sys.argv[1]).lower()
    char_set = sorted(set(input_string))
    print('Char count:')
    for element in char_set:
        count = input_string.count(element)
        print("{} = {}".format(element, count))
