# import re

# with open("/home/laufer/Desktop/python/day5/almanac.txt", 'r') as file:
#     _str = ''
#     inflist = []
#     line = file.readline()
#     inflist.append(re.sub(r"[^\d\s]", "", line).strip('\n'))
#     while True:
#         line = file.readline()
#         if not line:
#             inflist.append(re.sub(r"[^|\d\s]", "", _str))
#             break
#         if line == '\n':
#             inflist.append(re.sub(r"[^|\d\s]", "", _str))
#             _str = ''
#             continue
#         else:
#             line = line.strip('\n')
#             _str = _str + line + '|'
#         # break

# file.close()

# inflist = [i for i in inflist if i]

# seeds = list(filter(None, inflist[0].split(' ')))

# seed_to_soil_map = list(filter(None, inflist[1].split('|')))
# del seed_to_soil_map[0]

# soil_to_fertilizer_map =list(filter(None, inflist[2].split('|')))
# del soil_to_fertilizer_map[0]

# fertilizer_to_water_map = list(filter(None, inflist[3].split('|')))
# del fertilizer_to_water_map[0]

# water_to_light_map = list(filter(None, inflist[4].split('|')))
# del water_to_light_map[0]


# light_to_temperature_map = list(filter(None, inflist[5].split('|')))
# del light_to_temperature_map[0]

# temperature_to_humidit_map = list(filter(None, inflist[6].split('|')))
# del temperature_to_humidit_map[0]

# humidity_to_location_map = list(filter(None, inflist[7].split('|')))
# del humidity_to_location_map[0]

# total = []

# def f(seed, _list):
#     _f = ''
#     for i in _list:
#         i = i.split(' ')
#         if seed >= int(i[1]) and int(i[1]) + int(i[2]) >= seed:
#             _f = i
#             break
#     if _f != '':
#         return seed + int(_f[0]) - int(_f[1])
#     else:
#         return seed
    


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
#     # print(seed)

# # for i in range(len(seeds)):
# #     mini = 0
# #     seed = int(seeds[i])
# #     # print(seed)
# #     needstr = ''

# #     for c in seed_to_soil_map:
# #         c = c.split(' ')
# #         # print(c)

# #         if seed - int(c[1]) < 0:
# #             continue
# #         elif seed - int(c[1]) > mini:
# #             mini = seed - int(c[1])
# #             needstr = c
        
# #     if needstr == '':
# #         pass
# #     else:
# #         seed = seed + int(needstr[1]) - int(needstr[2])

# #     # print(seed)

# #     ######

# #     def func(seed, soil_to_fertilizer_map):
# #         a = soil_to_fertilizer_map[0].split(' ')
# #         if seed >  int(a[0]):
# #             mini = seed
# #         else:
# #             mini = seed
# #         # print(seed)
# #         # print(a)
# #         # print(mini)
# #         needstr = ''
# #         for c in soil_to_fertilizer_map:
# #             c = c.split(' ')
# #             # print(c)
# #             if seed - int(c[1]) < 0:
# #                 continue
# #             elif seed - int(c[1]) <= mini:
# #                 mini = seed - int(c[1])
# #                 needstr = c
            

# #         # print(needstr)
# #         # print(seed)
# #         # print(int(needstr[1]) + int(needstr[2]))
# #         if needstr == '':
# #             return seed
# #         if seed > int(needstr[1]) + int(needstr[2]):
# #             return seed
# #         else:

# #             return seed + int(needstr[0]) - int(needstr[1])



# #     seed = func(seed, soil_to_fertilizer_map)
# #     # print(seed)

# #     seed = func(seed, fertilizer_to_water_map)
# #     # print(seed)

# #     seed = func(seed, water_to_light_map)
# #     # print(seed)


# #     seed = func(seed, light_to_temperature_map)
# #     # print(seed)

# #     seed = func(seed, temperature_to_humidit_map)
# #     # print(seed)
# #     # # # print(temperature_to_humidit_map)

# #     # # # print(humidity_to_location_map)
# #     seed = func(seed, humidity_to_location_map)
# #     # print(seed)

# #     total.append(seed)





# # minelem = min(total)
# # print(minelem)
# # print(total)





# # seeds = list(filter(None, inflist[0].split(' ')))

# # seed_to_soil_map = list(filter(None, inflist[1].split('|')))
# # del seed_to_soil_map[0]

# # def func(ex, seeds) -> list:
# #     _list = [0] * 100
# #     tmplist = []
# #     for c in ex:
# #         tmp = c.split(' ')
# #         # print(tmp)
# #         for i in range(int(tmp[2])):
# #             _list[int(tmp[1]) + i] = int(tmp[0]) + i
# #             # print(i)

# #     for i in range(len(_list)):
# #         if _list[i] == 0:
# #             _list[i] = i

# #     for c in seeds:
# #         pos = _list[int(c)]
# #         # print(c, pos)
# #         tmplist.append(pos)
# #     print(_list)

# #     return tmplist    


# # ######## 

# # step1 = func(seed_to_soil_map, seeds)



# # soil_to_fertilizer_map =list(filter(None, inflist[2].split('|')))
# # del soil_to_fertilizer_map[0]
# # step2 = func(soil_to_fertilizer_map, step1)
# # print(step2)

# # fertilizer_to_water_map = list(filter(None, inflist[3].split('|')))
# # del fertilizer_to_water_map[0]
# # step3 = func(fertilizer_to_water_map, step2)
# # # print(step3)

# # water_to_light_map = list(filter(None, inflist[4].split('|')))
# # del water_to_light_map[0]
# # step4 = func(water_to_light_map, step3)
# # # print(step4)


# # light_to_temperature_map = list(filter(None, inflist[5].split('|')))
# # del light_to_temperature_map[0]
# # step5 = func(light_to_temperature_map, step4)
# # # print(step5)

# # temperature_to_humidit_map = list(filter(None, inflist[6].split('|')))
# # del temperature_to_humidit_map[0]
# # step6 = func(temperature_to_humidit_map, step5)
# # # print(step6)

# # humidity_to_location_map = list(filter(None, inflist[7].split('|')))
# # del humidity_to_location_map[0]
# # step7 = func(humidity_to_location_map, step6)
# # print(step7)

# # print(mini(step7))


# # # print(len(seed_to_soil_map))

# # # max = 0

# # # for c in seed_to_soil_map:
# # #     c = c.split(' ')
# # #     int(c[1]) + int(c[2])

# # #     if int(c[1]) + int(c[2]) > max:
# # #         print(max)
# # #         max = int(c[1]) + int(c[2])

# # # print(max)








import math
import os, sys
import time
from typing import List

class SeedMap:
    def __init__(self, off: str, to: str):
        self.off = off
        self.to = to
        self.map_values: list[tuple[int, int, int]] = []
    # ranges are non-overlapping
    def add(self, target: int, source: int, offset: int):
        self.map_values.append((source, source + offset, target))
    def sort(self):
        self.map_values.sort(key=lambda x: x[0])
    def get_destination(self, ranges: "SeedRangeList"):
        new_ranges = SeedRangeList()
        # for each range of seeds
        for start, end in ranges:
            # if we fully mapped the range, we can continue with next range
            found_mapping = False
            # for each mapping range
            for source, max_source, target in self.map_values:
                if start < source:
                    if end < source:
                        # ---- start -- end -- source -- max_source ----
                        new_ranges.add(start, end)
                        found_mapping = True
                        break
                    if end <= max_source:
                        # ---- start -- source -- end -- max_source ----
                        new_ranges.add(start, source)
                        # ---- target -- target + (end - source) -- target + (max_source - source) ----
                        new_ranges.add(target, target + (end - source))
                        found_mapping = True
                        break
                    # ---- start -- source -- max_source -- end ----
                    new_ranges.add(start, source)
                    # ---- target -- target + (max_source - source) ----
                    new_ranges.add(target, target + (max_source - source))
                    # we continue with the rest of the range
                    start = max_source
                # else if start is in between map range
                elif source <= start < max_source:
                    # if end is in between range
                    if end <= max_source:
                        # we map all
                        # ---- source -- start -- end -- max_source ----
                        # ---- target -- target + (start - source) -- target + (end - source) -- target + (max_source - source) ----
                        new_ranges.add(target + (start - source), target + (end - source))
                        found_mapping = True
                        break
                    # else if end is after this range
                    # we map until max_source
                    # ---- source -- start -- max_source -- end ----
                    # ---- target -- target + (start - source) -- target + (max_source - source) -- target + (end - source) ----
                    new_ranges.add(target + (start - source) , target + (max_source - source))
                    # we continue with the rest of the range
                    start = max_source
                # else if start is after range
                # we continue with the rest of the range
            # if we didn't find a mapping, we add the remaining range
            if not found_mapping:
                new_ranges.add(start, end)
        return new_ranges
    def __str__(self) -> str:
        return f"{self.off} => {self.to}"
    def __repr__(self) -> str:
        return self.__str__()

class SeedRangeList(List):
    def __init__(self):
        # start inclusive, end exclusive
        self.ranges: list[tuple[int, int]] = []
    def add(self, start: int, end: int):
        # for each already added range
        for i, (s, e) in enumerate(self.ranges):
            # if start is before range
            if start < s:
                # if end is before range
                if end < s:
                    # ---- start -- end -- s -- e ----
                    # we can add this range
                    self.ranges.insert(i, (start, end))
                    return
                # else if end is in between range
                if end <= e:
                    # we add only until s
                    # ---- start -- s -- end -- e ----
                    self.ranges.insert(i, (start, s))
                    return
                # else if end is after range
                # we add only until s
                # ---- start -- s -- e -- end ----
                self.ranges.insert(i, (start, s))
                # we continue with the rest of the range
                start = e
            # else if start is in between range
            elif start <= s <= end:
                # if end is in between range
                if end <= e:
                    # we already have this range
                    # ---- s -- start -- end -- e ----
                   return
                # else if end is after this range
                # we continue with the rest of the range
                # ---- s -- start -- e -- end ----
                start = e
            # else if start is after range
            # we continue with the rest of the range
            # ---- s -- e -- start -- end ----
        # if we haven't returned yet, we add the remaining range
        self.ranges.append((start, end))
    def __iter__(self):
        return iter(self.ranges)
    def __str__(self) -> str:
        return str(self.ranges)
    def __repr__(self) -> str:
        return self.__str__()


def main():
    with open(os.path.join(sys.path[0],"almanac.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    lines = text.split("\n")
    seed_range = lines[0].split(": ")[1].split(" ")
    seeds = SeedRangeList()
    for i in range(0, len(seed_range), 2):
        # add the range to the list
        seeds.add(int(seed_range[i]), int(seed_range[i]) + int(seed_range[i+1]))
    # create list of seed maps
    seed_maps: list[SeedMap] = []
    # start reading first map
    current_map = None
    # for each line after seeds
    for line in lines[1:]:
        # skip empty lines
        if line == "":
            continue
        # if new map declaration begins
        if line.endswith("map:"):
            # get from and to strings (just for printing)
            off, to = line.split(" ")[0].split("-to-", 1)
            # create new map
            current_map = SeedMap(off, to)
            # and add it to the list
            seed_maps.append(current_map)
        else:
            # if not new map declaration, add the mapping
            current_map.add(*[int(s) for s in line.split(" ")])
    for seed_map in seed_maps:
        seed_map.sort()
    
    # for each mapping
    for seed_map in seed_maps:
        print(seed_map)
        # map all seed ranges to new destination
        seeds = seed_map.get_destination(seeds)
    
    # print the minimum location, which will be the start of a range
    print(min([start for start, _ in seeds]))
            

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f} seconds")