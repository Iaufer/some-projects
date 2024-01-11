f = open('game_input.txt', 'r')

nred = 12
ngreen = 13
nblue = 14
red = 0
green = 0
blue = 0

sum = 0

while True:
    green = 0
    blue = 0
    red = 0
    line = f.readline()

    if not line:
        break
    game = line.split(":")
    print(game[0])
    _line = game[1].split(";")
    print(_line)
    _f = 1
    for c in _line:
        c = c.split(",")
        print(c)
        
        for _c in c:
            if "red" in _c:
                s1 = int("".join(a for a in _c if a.isdecimal()))
                if s1 > red:
                    red = s1
                if s1 > nred:
                    _f = 0
                # print("kolvo red is ", s1)
            if "green" in _c:
                s1 = int("".join(a for a in _c if a.isdecimal()))
                if s1 > green:
                    green = s1
                if s1 > ngreen:
                    _f = 0
                # print("kolvo green is ", s1)
            if "blue" in _c:
                s1 = int("".join(a for a in _c if a.isdecimal()))
                if s1 > blue:
                    blue = s1
                if s1 > nblue:
                    _f = 0
                # print("kolvo blue is ", s1)

    grb = green * blue * red
    print(grb)

    sum = sum + grb

    # if _f == 1:
    #     s1 = "".join(a for a in game[0] if a.isdecimal())
    #     sum = sum + int(s1)

    print(green, blue, red)

    
print(sum)


        

        # for _c in c:
        #     if "red" in _c:
        #         s1 = "".join(a for a in _c if a.isdecimal())
        #         print("kolvo red is ", s1)
        #         print(_c)
        #     if "green" in _c:
        #         s1 = "".join(a for a in _c if a.isdecimal())
        #         print("kolvo green is ", s1)
        #     if "blue" in _c:
        #         s1 = "".join(a for a in _c if a.isdecimal())
        #         print("kolvo blue is ", s1)
        #     break 