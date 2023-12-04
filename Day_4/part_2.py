games = {}
with open("Day_4/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        game, rest = line.split(":")
        game = game[4:]
        hand, wins = rest.split("|")
        hand, wins = [x for x in hand.split() if x != "" and x != " "], [x for x in wins.split() if x != "" and x != " "]
        games[str(int(game))] = {
                    "hand": hand,
                    "wins": wins,
                    "instances": 1
                }
    print(games["1"])

    for count in range(1, len(lines)+1):
        wins=0
        for num in games[str(count)]["hand"]:
            if num in games[str(count)]["wins"]:
                wins += 1
        for i in range(1, wins+1):
            games[str(count+i)]["instances"] += 1 * games[str(count)]["instances"]
        count += 1

    instances = 0
    for count in range(1, len(lines)+1):
        instances += games[str(count)]["instances"]
    print(instances)
