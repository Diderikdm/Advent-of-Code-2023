with open("day02.txt") as file:
    data = file.read().splitlines()
    p1 = {"red": 12, "green": 13, "blue": 14}
    games = {}
    for e, row in enumerate(data):
        games[e + 1] = {}
        for i, rounds in enumerate(row.split(":")[1].strip().split(";")):
            games[e + 1][i] = {}
            for blocks in rounds.strip().split(","):
                amount, color = blocks.strip().split()
                games[e + 1][i][color] = int(amount)
    r1 = sum(k for k, game in games.items() if all(round.get("red", 0) <= p1["red"] and round.get("green", 0) <= p1["green"] and round.get("blue", 0) <= p1["blue"] for round in game.values()))
    r2 = 0
    for game_number, game in games.items():
        r, g, b = 0, 0, 0
        for round in game.values():
            r = max(r, round.get("red", 0))
            g = max(g, round.get("green", 0))
            b = max(b, round.get("blue", 0))
        r2 += r * g * b
    print(f"p1: {r1}, p2: {r2}")