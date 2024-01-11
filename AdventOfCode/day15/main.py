with open('file.txt', 'r') as file:
    line = file.readline().split(',')

print(len(line))

def func_for_sub(line) -> int:
    sum = 0
    for i in range(len(line)):
        # if i == 0:
            # sum = (sum + ord(line[i]) * 17) % 256
        # else:
        sum = ((sum + ord(line[i])) * 17) % 256
    return sum 

def func(line) -> list:
    s = []
    for c in line:
        s.append(func_for_sub(c))

    return s

print((func(line)))  

print(len(set(line)))