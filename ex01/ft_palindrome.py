import sys

def is_palindrome(a):
    if a==a[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Error! Insert just 1 string!')
    else:
        s=str(sys.argv[1])
        mod = s.replace(" ","")
        if is_palindrome(mod)==True:
            print(f'The string {sys.argv[1]} is palindrome')
        else:
            print(f'The string {sys.argv[1]} is not palindrome')

