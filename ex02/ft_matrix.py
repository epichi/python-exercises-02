import sys

if len(sys.argv) != 3:
    print('Error! Usage: python3 ft_matrix.py <n> <m>')
else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    matrix = [[0 for i in range(m)] for j in range(n)]
    for r in range(n):
        for c in range(m):
            matrix[r][c] = float(
                input(f'Insert the element in position ({r}, {c}): '))
    print("The inserted matrix is:")
    for r in range(n):
        print(matrix[r])
    print("The sum over rows is: ")
    sum_rows = []
    for r in range(n):
        rows = 0
        for c in range(m):
            rows += matrix[r][c]
        sum_rows.append(rows)
    print(sum_rows)
    print("The sum over columns is: ")
    sum_cols = []
    for c in range(m):
        cols = 0
        for r in range(n):
            cols += matrix[r][c]
        sum_cols.append(cols)
    print(sum_cols)
