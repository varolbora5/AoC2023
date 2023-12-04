import numpy as np
with open("Day_1/input.txt") as file:
    strs = file.readlines()
    nums = []
    for line in strs:
        first = None
        last = None
        x, y = 0, -1
        while first == None:
            try:
                int(line[x])
                first = line[x]
                break
            except Exception:
                try:
                    if line[x:x+3] == "one":
                        first = "1"
                        break
                    elif line[x:x+3] == "two":
                        first = "2"
                        break
                    elif line[x:x+5] == "three":
                        first = "3"
                        break
                    elif line[x:x+4] == "four":
                        first = "4"
                        break
                    elif line[x:x+4] == "five":
                        first = "5"
                        break
                    elif line[x:x+3] == "six":
                        first = "6"
                        break
                    elif line[x:x+5] == "seven":
                        first = "7"
                        break
                    elif line[x:x+5] == "eight":
                        first = "8"
                        break
                    elif line[x:x+4] == "nine":
                        first = "9"
                        break
                except Exception:
                    pass
                x += 1
        while last == None:
            try:
                int(line[y])
                last = line[y]
                break
            except Exception:
                try:
                    if line[y-3:y] == "one":
                        last = "1"
                        break
                    elif line[y-3:y] == "two":
                        last = "2"
                        break
                    elif line[y-5:y] == "three":
                        last = "3"
                        break
                    elif line[y-4:y] == "four":
                        last = "4"
                        break
                    elif line[y-4:y] == "five":
                        last = "5"
                        break
                    elif line[y-3:y] == "six":
                        last = "6"
                        break
                    elif line[y-5:y] == "seven":
                        last = "7"
                        break
                    elif line[y-5:y] == "eight":
                        last = "8"
                        break
                    elif line[y-4:y] == "nine":
                        last = "9"
                        break
                except Exception:
                    pass
                y -= 1
        nums.append(int(first + last))
    print(nums)
    print(np.array(nums).sum())
