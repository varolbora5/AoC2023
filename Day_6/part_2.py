time = 53897698
distance = 313109012141201

ways_to_win = 1
wins = []
for time_spent in range(time):
    if time_spent * (time - time_spent) > distance:
        wins.append(time_spent)
ways_to_win = ways_to_win * len(wins)
print(ways_to_win)
