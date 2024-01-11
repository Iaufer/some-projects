inflist = []
dict_card = {'A': 13, 'K': 12, 'Q' : 11, 'J' : 0, 'T' : 9, '9' : 8, '8' : 7, '7' : 6, '6' : 5, '5' : 4, '4' : 3, '3' : 2, '2' : 1}
##############################
five = []
four = []
full_house = []
three = []
two = []
one = []
high = []
##############################
with open("/home/laufer/Desktop/python/day7/file.txt", 'r') as file:    
    while True:
        line = file.readline()
        if not line:
            break
        line = line.rstrip('\n')
        inflist.append(line)
# print(inflist   )
def determine_type(inflist):
    for c in inflist:
        listcount = []
        # c = "1111j"
        tmp = c.split(' ')
        # print(type(tmp))
        for i in range(len(tmp[0])):
            # print(tmp[0].count(tmp[0][i]))
            count = tmp[0].count(tmp[0][i])
            listcount.append(count)
        # print(listcount)
        if listcount.count(2) == 4:
            if tmp[0].count('J') == 1:
                full_house.append(tmp[0])
            elif tmp[0].count('J') == 2:
                four.append(tmp[0])
            else:
                two.append(tmp[0])
        if listcount.count(2) == 2 and listcount.count(1) == 3:
            if 'J' in tmp[0]:
                three.append(tmp[0])
            else:
                one.append(tmp[0])
        if listcount.count(3) == 3 and listcount.count(1)  == 2:
            if 'J' in tmp[0]:
                four.append(tmp[0])
            else:
                three.append(tmp[0])
        if listcount.count(2) == 2 and listcount.count(3) == 3:
            if 'J' in tmp[0]:
                five.append(tmp[0])
            else:
                full_house.append(tmp[0])
        if listcount.count(5) == 5:
            five.append(tmp[0])
        if listcount.count(4) == 4 and listcount.count(1) == 1:
            if 'J' in tmp[0]:
                five.append(tmp[0])
                # print("five")
            else:
                four.append(tmp[0])

        if listcount.count(1) == 5:
            if 'J' in tmp[0]:
                one.append(tmp[0])
            else:
                high.append(tmp[0])
        # print(listcount.count(2))
        # break
    return five, four, full_house, three, two, one, high

        # print(tmp[0].count('2'), len(tmp[0]))


def compare(s1, s2):
    for i in range(len(s1)):
        o1 = dict_card[s1[i]]
        o2 = dict_card[s2[i]]
        if o1 != o2:
            return o1 > o2
    return False


def sort_hands_list(hand_list):
    for i in range(len(hand_list)):
        for j in range(i + 1, len(hand_list)):
            if compare(hand_list[i], hand_list[j]):
                hand_list[i], hand_list[j] = hand_list[j], hand_list[i]
    return hand_list




five, four, full_house, three, two, one, high = determine_type(inflist)
# determine_rang_for_two(two)

one = sort_hands_list(one)
two = sort_hands_list(two)
three = sort_hands_list(three)
four = sort_hands_list(four)
five = sort_hands_list(five)
full_house = sort_hands_list(full_house)
high = sort_hands_list(high)


print(high)
print(one)
print(two)
print(three)
print(full_house)
print(four)
print(five)

res = high + one + two + three + full_house + four + five
# print(res)
# print(inflist)


am = []

for c in res:
    for x in inflist:
        if c in x:
            am.append(x.split(' ')[1])
            break

sum = 0
# print(am)

for i in range(len(am)):
    sum = sum + ((i + 1) * int(am[i]))
    # print(i + 1, am[i])

print(sum)