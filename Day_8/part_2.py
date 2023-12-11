import re
directions = "LLRLRRRLLLRLRRLRRRLRLRRLRLRLRRRLRRRLRLRLRRLLRRRLRRLRRLLRLRRRLRLRLLRRRLLRRRLRLRRRLRRRLRRRLLLRRRLRRLRRLRLRRLRLRRRLRLRRLRLRLRRRLRLLLRRRLLLRLRRRLRLRRLRLRLRLRRLRRLRRLRLRRRLRRRLRRLRRRLRRLRRLRRRLLRLRRLLLRRLRRLRLRLLLRRLRRLRRRLRRLLRLRRRLRRRLRRLRRLRLRRLRLRRRLRRLRRRLLRRRLRLRLLLRRRLLLRRLLRRLRLRRLRLLLRRRR"

links = {}
starts = []

with open("Day_8/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        node, rest = line.split("=")
        node = re.sub(" ", "", node)
        if node.endswith("A"):
            starts.append(node)
        rest = re.sub(r"\(|\)|\ |\n", "", rest)
        left, right = rest.split(",")
        links[node] = {"L": left,
                         "R": right}


iters = 0
while True:
    for idx, curr in enumerate(starts):
        starts[idx] = links[curr][directions[iters%len(directions)]]
    for node in starts:
        if node
    iters += 1
print(iters)
