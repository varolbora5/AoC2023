with open("Day_4/input.txt") as file:
    lines = file.readlines()
    game_score = 0
    for line in lines:
        _, game = line.split(":")
        hand, wins = game.split("|")
        hand, wins = [x for x in hand.split() if x != "" and x != " "], [x for x in wins.split() if x != "" and x != " "]
        score = 0
        for num in hand:
            if num in wins:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
        game_score += score
    print(game_score)
