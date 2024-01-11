with open("/home/laufer/Desktop/python/day6/file.txt", 'r') as file:
    _line1 = file.readlines()
file.close()


line1 = "".join(c for c in _line1[0] if c.isdecimal())
line2 = "".join(c for c in _line1[1] if c.isdecimal())

j = 0

line1 = int(line1)
line2 = int(line2)
for i in range(1, line1):
    print(1)
    if (line1 - i) * i  > line2:
        j = j + 1

print(j)
