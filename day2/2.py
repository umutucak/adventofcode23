def p1():
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0
    impossible = False
    for game in open("2.input", "r"):
        id = int(game.split(":")[0].split()[1])
        game = game.split(":")[1].split(";") # toss out game x, then split the sets
        for show in game:
            if impossible:
                break
            show = show.split(",")
            for cube in show:
                cube = cube.split()
                if int(cube[0]) > limits[cube[1]]:
                    print("game", id, "is impossible")
                    impossible = True
                    break
        if not impossible:
            sum += id
        impossible = False

    print(sum)

def p2():
    power = 0
    for game in open("2.input", "r"):
        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game = game.split(":")[1].split(";") # toss out game x, then split the sets
        for show in game:
            show = show.split(",")
            for cube in show:
                cube = cube.split()
                if int(cube[0]) > minimums[cube[1]]:
                    minimums[cube[1]] = int(cube[0])
        power += minimums["red"] * minimums["green"] * minimums["blue"]
    print(power)

p2()