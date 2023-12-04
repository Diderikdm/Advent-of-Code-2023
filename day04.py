with open("day04.txt") as file:
    data = file.read().splitlines()
    r1, cards = 0, {}
    for row in data:
        card, numbers = row.split(":")
        cards[card] = cards.get((card := int(card.split()[1].strip())), 0) + 1
        winning, own = numbers.split("|")
        if (overlap := {int(x) for x in winning.split() if x} & {int(x) for x in own.split() if x}):
            r1 += (2 ** (len(overlap) - 1))
            for c in range(card + 1, card + len(overlap) + 1):
                cards[c] = cards.get(c, 0) + cards[card]
    print(f"p1: {r1}, p2: {sum(cards.values())}")

# Oneliner
print((r1,sum(c))if all([not(r1:=0),(c:=[1]*len(data)),(y:=lambda s:{int(x)for x in s.split()if x}),[x for e,x in enumerate(open("day04.txt").read().splitlines())if(o:=y((w:=x.split(":")[1].split("|"))[0])&y(w[1]))and(r1:=r1+(2**(len(o)-1)))and[c.insert(d,c.pop(d)+1*c[e])for d in range(e+1,e+len(o)+1)]]])else 0)