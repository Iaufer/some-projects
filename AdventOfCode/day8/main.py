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
def route(_dict, path):
    i = 0
    count = 0
    next = 'AAA'
    # print(path)
    while True:
        if next == 'ZZZ':
            return count
        # print(_dict.get(next), _dict[next])
        if i == len(path):
            i = 0
        t = _dict.get(next)

        if path[i] == 'R':
            tmp = t.split(' ')
            next = tmp[2]
            # print(next)
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

print(route(sorted_dict, path))





# print(inflist)
# # print(len(path))
# def route(inflist, path):
#     i = 0
#     next = 'AAA'
#     for c in inflist:
#         if next in c[0]:
#             if 'ZZZ' in next:
#                 return i
#             if i == len(path) and next != 'ZZZ':
#                 path += path[i-2]
#             if path[i] == 'R':
#                 next = re.sub(r'[^a-zA-Z\s]', '', c[1]).split(' ')[2]             
#                 print(next)
#                 i += 1
#             elif path[i] == 'L':
#                 next = re.sub(r'[^a-zA-Z\s]', '', c[1]).split(' ')[1]
#                 print(next)
#                 i += 1

#     return i

