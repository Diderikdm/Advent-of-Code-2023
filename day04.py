with open("day04.txt") as file:
    data = file.read().splitlines()
    r1, r2, cards = 0, 0, {}
    for row in data:
        card, numbers = row.split(":")
        cards[card] = cards.get((card := int(card.split()[1].strip())), 0) + 1
        winning, own = numbers.split("|")
        if (overlap := {int(x) for x in winning.split() if x} & {int(x) for x in own.split() if x}):
            r1 += (2 ** (len(overlap) - 1))
            r2 += 1 << sum(row.split().count(x) == 2 for x in row.split() if x) // 2 >> 1
            for c in range(card + 1, card + len(overlap) + 1):
                cards[c] = cards.get(c, 0) + cards[card]
    print(f"p1: {r1}, p2: {sum(cards.values())}")