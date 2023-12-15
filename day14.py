with open("day14.txt", "r") as file:
    data = tuple(map(tuple, file.read().splitlines()))
    reverse = tuple(map(tuple, zip(*data)))
    w = {i : [e for e, y in enumerate(x) if y == "#"] for i, x in enumerate(data)}
    h = {i : [e for e, y in enumerate(x) if y == "#"] for i, x in enumerate(reverse)}
    seen, c, p1 = [], 0, 0
    get_current = lambda x: ((reverse, h), (data, w))[x % 2]
    while (nxt := tuple(map(tuple, zip(*reverse)))) not in seen:
        seen.append(nxt)
        for direction in range(4):
            current, blocks =  get_current(direction)
            new_r = []
            for e, row in enumerate(current):
                new, prev, static = [], 0, blocks[e]
                for i in static:
                    new += sorted(row[prev : i], key = lambda x: x != ["O", "."][direction in [2, 3]]) + ["#"]
                    prev = i + 1
                new_r.append(new + sorted(row[prev : len(row)], key = lambda x: x != ["O", "."][direction in [2, 3]]))
            if current == reverse:
                data = tuple(map(tuple, zip(*new_r)))
            else:
                reverse = tuple(map(tuple, zip(*new_r)))
            if not p1 and not direction:
                p1 = sum([data[u].count("O") * -u for u in range(-len(data), 0)])
        c += 1
    nxt = seen[(s := seen.index(nxt)) + (1000000000 - s) % (c - s)]
    print(p1, sum([nxt[e].count("O") * -e for e in range(-len(nxt), 0)]))