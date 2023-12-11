import re
directions = "LLRLRRRLLLRLRRLRRRLRLRRLRLRLRRRLRRRLRLRLRRLLRRRLRRLRRLLRLRRRLRLRLLRRRLLRRRLRLRRRLRRRLRRRLLLRRRLRRLRRLRLRRLRLRRRLRLRRLRLRLRRRLRLLLRRRLLLRLRRRLRLRRLRLRLRLRRLRRLRRLRLRRRLRRRLRRLRRRLRRLRRLRRRLLRLRRLLLRRLRRLRLRLLLRRLRRLRRRLRRLLRLRRRLRRRLRRLRRLRLRRLRLRRRLRRLRRRLLRRRLRLRLLLRRRLLLRRLLRRLRLRRLRLLLRRRR"

links = {}

with open("Day_8/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        node, rest = line.split("=")
        node = re.sub(" ", "", node)
        rest = re.sub(r"\(|\)|\ |\n", "", rest)
        left, right = rest.split(",")
        links[node] = {"L": left,
                         "R": right}
curr = "AAA"
iters = 0
while True:
    if curr == "ZZZ": break
    curr = links[curr][directions[iters%len(directions)]]
    iters += 1
print(iters)
