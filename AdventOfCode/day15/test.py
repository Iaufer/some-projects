with open('/home/laufer/Desktop/Labs/AdventOfCode/day15/k.txt', 'r') as file:
    line = file.readline().split(',')



_dict = {}

def func_for_sub(line) -> int:
    sum = 0
    for i in range(len(line)-2):
        sum = ((sum + ord(line[i])) * 17) % 256
    if sum not in _dict:
        _dict[sum] = []
    
    f = 0
    if sum in _dict:
        value = _dict[sum]
        for i, item in enumerate(value):
            if line[:2] in item:
                value[i] = line.replace('=', ' ')
                f = 1

    if f != 1:
        _dict[sum].append(line.replace('=', ' '))
    
    return sum 



def func_for_sub_minus(line) -> int:
    sum = 0
    for i in range(len(line) - 1):
        sum = ((sum + ord(line[i])) * 17) % 256

    if sum not in _dict:
        _dict[sum] = []

    for item in _dict[sum]:
        # print(item) 
        if line[:-1] in item:
            _dict[sum].remove(item)  
    
    return sum

def func(line) -> list:
    s = []
    for c in line:
        if '=' in c:
            s.append(func_for_sub(c))
        elif '-' in c:
            s.append(func_for_sub_minus(c))
        # break
    return s

print((func(line)))  


print(_dict)


sum = 0

for key, value in _dict.items():
    res = 1
    for i in  range(len(value)):
        tmp = value[i].split(' ')
        res = (key + 1) * (i+1) * int(tmp[1])
        sum += res
        # print((key + 1), i +1 , (tmp[1]))
        # break
        print(res)
print(sum)