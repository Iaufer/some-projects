import re

inflist = []
_dict = {}
with open("/home/laufer/Desktop/python/day8/file.txt", 'r') as file:    
    path = file.readline().rstrip('\n')
    while True:
        line = file.readline()
        if not line:
            break
        if line == '\n':
            continue
        line = line.rstrip('\n').split('=')
        _dict[re.sub(r'[^a-zA-Z]', '', line[0])] = re.sub(r'[^a-zA-Z\s]', '', line[1]) 


# print(path)
# print(_dict)

tmplist = []
def ls(_dict):
    for key in _dict:
        if 'A' in key:
            tmplist.append(key)
            # print(key)

    return tmplist


def route(_dict, path, tmplist):
    # print(tmplist)

    i = 0
    count = 0
    next = tmplist
    # print(path)
    while True:
        if 'Z' in next:
            print(next)
            print(count)
            return count
        # print(_dict.get(next), _dict[next])
        if i == len(path):
            i = 0
        t = _dict.get(next)

        if path[i] == 'R':
            tmp = t.split(' ')
            next = tmp[2]
            # print(next)/
            i += 1
            count += 1
        elif path[i] == 'L':
            tmp = t.split(' ')
            next = tmp[1]
            # print(next)
            count += 1
            i += 1      
    return count


sorted_dict = {key: value for key, value in sorted(_dict.items())}
tmplist = ls(_dict)
# print(route(sorted_dict, path, tmplist))
# print(len(ls(_dict)))

r0 = route(_dict, path, tmplist[0])
r1 = route(_dict, path, tmplist[1])
r2 = route(_dict, path, tmplist[2])
r3 = route(_dict, path, tmplist[3])
r4 = route(_dict, path, tmplist[4])
r5 = route(_dict, path, tmplist[5])
