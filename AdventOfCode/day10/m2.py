
rows = 140
cols = 140

with open("/home/laufer/Desktop/python/day10/file.txt", 'r') as file:    
    line = [item.rstrip('\n') for item in file.readlines()]


def fill_matrix(line):
    matrix = []

    for i in range(rows):
        matrix.append([])
        tmp = line[i]
        for j in range(cols):
            matrix[i].append(tmp[j])

    return matrix
    # print(matrix[i])
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))



ma = []

for i in range(rows):
    ma.append([])
    # tmp = line[i]
    for j in range(cols):
        ma[i].append('-')


def find_S(matrix):

    target_value = 'S' # Значение, которое вы ищете

    found = False
    target_row = -1
    target_col = -1

    for i, row in enumerate(matrix):
        if target_value in row:
            target_row = i
            target_col = row.index(target_value)
            found = True
            break

    # if found:
    #     print(f"Элемент {target_value} найден в позиции ({target_row}, {target_col})")
    # else:
    #     print(f"Элемент {target_value} не найден в матрице")


    # print(matrix[target_row][target_col])

    return target_row, target_col

def direct(i, j, matrix):
    if matrix[i-1][j] == '|' or matrix[i-1][j] == 'F' or matrix[i-1][j] == '7':
        
        i -= 1
        return 'u', i , j
    elif matrix[i+1][j] == '|' or matrix[i+1][j] == 'J' or matrix[i+1][j] == 'L':
        i += 1
        return 'd', i, j
    elif matrix[i][j+1] == '-' or matrix[i][j+1] == 'J' or matrix[i][j+1] == '7':
        j += 1
        return 'r', i, j
    elif matrix[i][j-1] == '|' or matrix[i][j-1] == 'F' or matrix[i][j-1] == 'L':
        j -= 1
        return 'l', i, j
    else:
        return ' '

def func(matrix):
    # r = 16
    i, j = find_S(matrix)
    # print(matrix[i][j])
    path, i, j = direct(i, j, matrix)
    # print(matrix[i][j], path)
    # path = direct(i, j, matrix)
    print(path)
    count = 0
    while True:
        ma[i][j] = '#'
        # print(path)
        count += 1
        # if r == 0:
            # print(matrix[i][j])
            # break

        print(matrix[i][j], path)
        if matrix[i][j] == 'S':
            break

        if path == 'd':
            if matrix[i][j] == 'L':
                j += 1
                path = 'r'
            elif matrix[i][j] == 'J':
                j -= 1
                path = 'l'
            elif matrix[i][j] == '|':
                i += 1
                path = 'd'
        elif path == 'r':
            if matrix[i][j] == '-':
                j += 1
                path = 'r'
            elif matrix[i][j] == '7':
                i += 1
                path = 'd'
            elif matrix[i][j] == 'J':
                i -= 1
                path = 'u'
        
        elif path == 'l':
            if matrix[i][j] == '-':
                j -= 1
                path = 'l'
            elif matrix[i][j] == 'L':
                i -= 1
                path = 'u'
            elif matrix[i][j] == 'F':
                i += 1
                path= 'd'

        elif path == 'u':
            if matrix[i][j] == '|':
                path = 'u'
                i -= 1
            elif matrix[i][j] == '7':
                j -= 1
                path = 'l'
            elif matrix[i][j] == 'F':
                j += 1    
                path = 'r'              
        # r -= 1
        # break    
    # print(matrix[i][j])



    print(count/2)
    print_matrix(ma)

matrix = fill_matrix(line)
# print_matrix(matrix)
# find_S(matrix)
i, j = find_S(matrix)

# print(direct(i, j, matrix))

func(matrix)
