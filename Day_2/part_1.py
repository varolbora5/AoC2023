import re
import numpy as np

with open("Day_2/input.txt") as file:
    lines = file.readlines()
    games = []
    for line in lines:
        [game, rest] = line.split(":")
        game = int(game[5:])
        sets = rest.split(";")
        cubes = []
        for _set in sets:
            piece = _set.split(",")
            for piece in piece:
                match piece.split(" "):
                    case ["", num, color, *fuck]:
                        cubes.append((re.sub("\n", "", color), int(num)))
                    case [num, color]:
                        cubes.append((re.sub("\n", "", color), int(num)))
        count = {
                "red": 0,
                "green": 0,
                "blue": 0,
                }
        for [color, num] in cubes:
            if count[color] < num:
                count[color] = num
        games.append(count["red"]*count["blue"]*count["green"])
    print(np.array(games).sum())
