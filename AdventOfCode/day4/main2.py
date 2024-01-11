f = open('input.txt', 'r')

xs = [0] * len(f.readlines())

listcount =[]

f.seek(0)
k = 1
while True:
    _count = 0
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


    for c in lc:
        if c in rc:
            _count = _count + 1

    listcount.append(_count)


    for i in range(k, k + _count):
        xs[i] += 1
    
    k += 1

for i in range(1, len(listcount)):
    k = i
    for j in range(k, listcount[i] + k):
        xs[j+1] += xs[k]

    print(xs)


print(sum(xs) + len(xs))


f.close()
            