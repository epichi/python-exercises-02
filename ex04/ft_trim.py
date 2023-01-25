import sys


def trim(p=[], has_return=False):
    l = len(p)
    f = p[1:(l-1)]
    if has_return:
        return f
    return None


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Error! You must insert at least 2 values')
    else:
        s = sys.argv[1:]
        p = []
        for element in s:
            p.append(element)
        print('The new list is: ', trim(p, True))
