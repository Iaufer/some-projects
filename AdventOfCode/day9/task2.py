
with open("/home/laufer/Desktop/python/day9/file.txt", 'r') as file:    
    line = [item.rstrip('\n') for item in file.readlines()]

def func(line1) -> int:
    reslist = []
    line1 = line1.split(' ')
    line1 = line1[::-1]


    while True:

        for i in range(len(line1)-1):
            line1[i] = int(line1[i+1]) - int(line1[i])

        reslist.append(int(line1[len(line1) - 1]))
        del line1[-1]
        # print(len(line1))
        if line1.count(0) == len(line1):
            break

    # print(line1)
    # print(reslist)
    tmp = sum(reslist)
    return tmp
# print((func(line[0]) + func(line[1]) + func(line[2])))

_sum = 0
# print(len(line))
# print((line))

for i in range(len(line)):
    print(func(line[i]))
    tmp = func(line[i])
    # print(tmp)
    _sum += tmp

print(_sum)
# print((line[0]))