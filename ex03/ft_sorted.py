import sys
if len(sys.argv) < 3:
    print('Error! You must insert at least 2 numbers')
else:
    l = []
    for n in sys.argv[1:]:
        l.append(int(n))
    a = sorted(l, reverse=True)
    if l == a:
        print('The inserted sequence is sorted!')
    else:
        print('The inserted sequence is not sorted!')
        print(f'The correct order is {a}')
