with open("day04.txt") as file:
    data = file.read().splitlines()
    cards, cards_p2 = set(), {}
    r1, r2 = 0, 0
    for row in data:
        card, numbers = row.split(":")
        cards.add((card := int(card.split()[1].strip())))
        cards_p2[card] = cards_p2.get(card, 0) + 1
        winning, own = numbers.split("|")
        if (overlap := {int(x) for x in winning.split() if x} & {int(x) for x in own.split() if x}):
            r1 += (2 ** (len(overlap) - 1))
            for c in range(card + 1, card + len(overlap) + 1):
                cards_p2[c] = cards_p2.get(c, 0) + cards_p2[card]
    r2 = sum(v for k, v in cards_p2.items() if k in cards)
    print(f"p1: {r1}, p2: {r2}")