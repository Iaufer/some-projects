import re

with open("/home/laufer/Desktop/python/day5/almanac.txt", 'r') as file:
    _str = ''
    inflist = []
    line = file.readline()
    inflist.append(re.sub(r"[^\d\s]", "", line).strip('\n'))
    while True:
        line = file.readline()
        if not line:
            inflist.append(re.sub(r"[^|\d\s]", "", _str))
            break
        if line == '\n':
            inflist.append(re.sub(r"[^|\d\s]", "", _str))
            _str = ''
            continue
        else:
            line = line.strip('\n')
            _str = _str + line + '|'
        # break

file.close()

inflist = [i for i in inflist if i]

seeds = list(filter(None, inflist[0].split(' ')))

seed_to_soil_map = list(filter(None, inflist[1].split('|')))
del seed_to_soil_map[0]

soil_to_fertilizer_map =list(filter(None, inflist[2].split('|')))
del soil_to_fertilizer_map[0]

fertilizer_to_water_map = list(filter(None, inflist[3].split('|')))
del fertilizer_to_water_map[0]

water_to_light_map = list(filter(None, inflist[4].split('|')))
del water_to_light_map[0]


light_to_temperature_map = list(filter(None, inflist[5].split('|')))
del light_to_temperature_map[0]

temperature_to_humidit_map = list(filter(None, inflist[6].split('|')))
del temperature_to_humidit_map[0]

humidity_to_location_map = list(filter(None, inflist[7].split('|')))
del humidity_to_location_map[0]

total = []


def f(seed, _list):
    _f = ''
    for i in _list:
        i = i.split(' ')
        if seed >= int(i[1]) and int(i[1]) + int(i[2]) >= seed:
            _f = i
            break
    if _f != '':
        return seed + int(_f[0]) - int(_f[1])
    else:
        return seed
    
mintot = []

def a1():

    for i in range(int(seeds[0]), int(seeds[0]) + int(seeds[1])):
        seed = i
        seed = f(seed, seed_to_soil_map)
        # print(seed)
        seed = f(seed, soil_to_fertilizer_map) 
        # print(seed)
        seed = f(seed, fertilizer_to_water_map) 
        # print(seed)

        seed = f(seed, water_to_light_map) 
        # print(seed)

        seed = f(seed, light_to_temperature_map) 
        # print(seed)

        seed = f(seed, temperature_to_humidit_map) 
        # print(seed)

        seed = f(seed, humidity_to_location_map)
        total.append(seed)

    a = min(total)
    mintot.append(a)
    print(1)
    total = []


def a2():


    for i in range(int(seeds[2]), int(seeds[2]) + int(seeds[3])):
        seed = i
        seed = f(seed, seed_to_soil_map)
        # print(seed)
        seed = f(seed, soil_to_fertilizer_map) 
        # print(seed)
        seed = f(seed, fertilizer_to_water_map) 
        # print(seed)

        seed = f(seed, water_to_light_map) 
        # print(seed)

        seed = f(seed, light_to_temperature_map) 
        # print(seed)

        seed = f(seed, temperature_to_humidit_map) 
        # print(seed)

        seed = f(seed, humidity_to_location_map)
        total.append(seed)

    a = min(total)
    mintot.append(a)
    print(2)

    total = []

print(mintot)

# for i in range(int(seeds[2]), int(seeds[2]) + int(seeds[3])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# a = min(total)
# mintot.append(a)

# total = []


# print(3)

# for i in range(int(seeds[4]), int(seeds[4]) + int(seeds[5])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# a = min(total)
# mintot.append(a)
# print(4)

# total = []

# for i in range(int(seeds[6]), int(seeds[6]) + int(seeds[7])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# a = min(total)
# mintot.append(a)
# print(5)

# total = []

# for i in range(int(seeds[8]), int(seeds[8]) + int(seeds[9])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# a = min(total)
# mintot.append(a)
# print(6)

# total = []

# for i in range(int(seeds[10]), int(seeds[11]) + int(seeds[12])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)


# a = min(total)
# mintot.append(a)
# print(7)

# total = []
# for i in range(int(seeds[13]), int(seeds[13]) + int(seeds[14])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)


# a = min(total)
# mintot.append(a)
# print(8)

# total = []
# for i in range(int(seeds[15]), int(seeds[15]) + int(seeds[16])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# a = min(total)
# mintot.append(a)
# print(9)

# total = []

# for i in range(int(seeds[17]), int(seeds[17]) + int(seeds[18])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# a = min(total)
# mintot.append(a)
# total = []

# print(10)

# for i in range(int(seeds[18]), int(seeds[18]) + int(seeds[19])):
#     seed = i
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)


# mini = min(mintot)
# print(mini)

# for i in range(len(seeds)):
#     seed = int(seeds[i])
#     seed = f(seed, seed_to_soil_map)
#     # print(seed)
#     seed = f(seed, soil_to_fertilizer_map) 
#     # print(seed)
#     seed = f(seed, fertilizer_to_water_map) 
#     # print(seed)

#     seed = f(seed, water_to_light_map) 
#     # print(seed)

#     seed = f(seed, light_to_temperature_map) 
#     # print(seed)

#     seed = f(seed, temperature_to_humidit_map) 
#     # print(seed)

#     seed = f(seed, humidity_to_location_map)
#     total.append(seed)

# _min = min(total)
# print(_min) 
    # print(seed)

# for i in range(len(seeds)):
#     mini = 0
#     seed = int(seeds[i])
#     # print(seed)
#     needstr = ''

#     for c in seed_to_soil_map:
#         c = c.split(' ')
#         # print(c)

#         if seed - int(c[1]) < 0:
#             continue
#         elif seed - int(c[1]) > mini:
#             mini = seed - int(c[1])
#             needstr = c
        
#     if needstr == '':
#         pass
#     else:
#         seed = seed + int(needstr[1]) - int(needstr[2])

#     # print(seed)

#     ######

#     def func(seed, soil_to_fertilizer_map):
#         a = soil_to_fertilizer_map[0].split(' ')
#         if seed >  int(a[0]):
#             mini = seed
#         else:
#             mini = seed
#         # print(seed)
#         # print(a)
#         # print(mini)
#         needstr = ''
#         for c in soil_to_fertilizer_map:
#             c = c.split(' ')
#             # print(c)
#             if seed - int(c[1]) < 0:
#                 continue
#             elif seed - int(c[1]) <= mini:
#                 mini = seed - int(c[1])
#                 needstr = c
            

#         # print(needstr)
#         # print(seed)
#         # print(int(needstr[1]) + int(needstr[2]))
#         if needstr == '':
#             return seed
#         if seed > int(needstr[1]) + int(needstr[2]):
#             return seed
#         else:

#             return seed + int(needstr[0]) - int(needstr[1])



#     seed = func(seed, soil_to_fertilizer_map)
#     # print(seed)

#     seed = func(seed, fertilizer_to_water_map)
#     # print(seed)

#     seed = func(seed, water_to_light_map)
#     # print(seed)


#     seed = func(seed, light_to_temperature_map)
#     # print(seed)

#     seed = func(seed, temperature_to_humidit_map)
#     # print(seed)
#     # # # print(temperature_to_humidit_map)

#     # # # print(humidity_to_location_map)
#     seed = func(seed, humidity_to_location_map)
#     # print(seed)

#     total.append(seed)




from threading import Thread


new_thread1 = Thread(target=a1)
new_thread2 = Thread(target=a2)

new_thread1.start()
new_thread2.start()


new_thread1.join()
new_thread2.join()


# minelem = min(total)
# print(minelem)
# print(total)





# seeds = list(filter(None, inflist[0].split(' ')))

# seed_to_soil_map = list(filter(None, inflist[1].split('|')))
# del seed_to_soil_map[0]

# def func(ex, seeds) -> list:
#     _list = [0] * 100
#     tmplist = []
#     for c in ex:
#         tmp = c.split(' ')
#         # print(tmp)
#         for i in range(int(tmp[2])):
#             _list[int(tmp[1]) + i] = int(tmp[0]) + i
#             # print(i)

#     for i in range(len(_list)):
#         if _list[i] == 0:
#             _list[i] = i

#     for c in seeds:
#         pos = _list[int(c)]
#         # print(c, pos)
#         tmplist.append(pos)
#     print(_list)

#     return tmplist    


# ######## 

# step1 = func(seed_to_soil_map, seeds)



# soil_to_fertilizer_map =list(filter(None, inflist[2].split('|')))
# del soil_to_fertilizer_map[0]
# step2 = func(soil_to_fertilizer_map, step1)
# print(step2)

# fertilizer_to_water_map = list(filter(None, inflist[3].split('|')))
# del fertilizer_to_water_map[0]
# step3 = func(fertilizer_to_water_map, step2)
# # print(step3)

# water_to_light_map = list(filter(None, inflist[4].split('|')))
# del water_to_light_map[0]
# step4 = func(water_to_light_map, step3)
# # print(step4)


# light_to_temperature_map = list(filter(None, inflist[5].split('|')))
# del light_to_temperature_map[0]
# step5 = func(light_to_temperature_map, step4)
# # print(step5)

# temperature_to_humidit_map = list(filter(None, inflist[6].split('|')))
# del temperature_to_humidit_map[0]
# step6 = func(temperature_to_humidit_map, step5)
# # print(step6)

# humidity_to_location_map = list(filter(None, inflist[7].split('|')))
# del humidity_to_location_map[0]
# step7 = func(humidity_to_location_map, step6)
# print(step7)

# print(mini(step7))


# # print(len(seed_to_soil_map))

# # max = 0

# # for c in seed_to_soil_map:
# #     c = c.split(' ')
# #     int(c[1]) + int(c[2])

# #     if int(c[1]) + int(c[2]) > max:
# #         print(max)
# #         max = int(c[1]) + int(c[2])

# # print(max)






