f = open('input.txt', 'r')


sum = 0
max = 0

while True:
    res = 0
    line = f.readline()
    if not line:
        break
    line = line.replace('\n', '')

    _line = line.split(":")

    count = _line[1].split("|")

    lc = count[0].split(" ")
    rc = count[1].split(" ")

    lc = [i for i in lc if i]
    rc = [i for i in rc if i]

    _f = 1
    for c in lc:
        if c in rc:
            print(c)
            if res == 0 and _f == 1:
                res = 1
                _f = 0
            else:
                res = res * 2

    if max < res:
        max = res

    sum = sum + int(res)


    print(lc)
    print(rc)

print(sum)