import re

with open("/home/laufer/Desktop/python/day6/file.txt", 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
file.close()

line1 = re.sub(r"[^\d\s]", "", line1).strip('\n').split(' ')
line1 = [i for i in line1 if i]

line2 = re.sub(r"[^\d\s]", "", line2).strip('\n').split(' ')
line2 = [i for i in line2 if i]

v = 0
mul = 1 
j = 1


for c, x in zip(line1, line2):
    v = 0
    j = 0
    # print(c, x)
    for i in range(int(c)):
        c = int(c) - 1
        v += 1
        # print(c * v) 
        if int(x) < c * v:
            j += 1
    mul *= j

print(mul)