races = [(53, 313), (89, 1090), (76, 1214), (98, 1201)]

ways_to_win = 1
for race in races:
    wins = []
    for time_spent in range(race[0]):
        if time_spent * (race[0] - time_spent) > race[1]:
            wins.append(time_spent)
    ways_to_win = ways_to_win * len(wins)
print(ways_to_win)
