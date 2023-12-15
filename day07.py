def sort(cards, joker, order):
    s = tuple(
        sum(
            [
                (cards.count(x) + [0, cards.count(joker)][not e]) == y
                for e, x in enumerate(sorted(set(cards) - {joker}, key=lambda z: -cards.count(z)))
            ]
        )
        for y in range(5, 0, -1)
    ) + tuple(order.index(x) for x in cards)
    return [s, (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)][not sum(s)]

with open("day07.txt", "r") as file:
    data = [x.split() for x in file.read().splitlines()]
    r = []
    for result, joker, order in ((0, " ", "23456789TJQKA"), (0, "J", "J23456789TQKA")):
        for e, (cards, score) in enumerate(sorted(data, key=lambda x: sort(x[0], joker, order))):
            result += (e + 1) * int(score)
        r.append(result)
    print(r)