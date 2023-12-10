def expand_collection(coords: set[tuple[int, int]]):
    for x, y in set(coords):
        others = {(x,y)}
        while others:
            X, Y = others.pop()
            adj = {a for x, y in (
                (X + 1, Y), (X- 1, Y), (X, Y + 1), (X, Y - 1)
                                                    ) if all([(a := (x, y)) in grid, 0 <= x < w, 0 <= y < h, a not in seen, a not in coords])}
            coords |= adj
            others |= adj
    return coords


with open("day10.txt", "r") as file:
    data = file.read().splitlines()
    start, h, w = 1, len(data), len(data[0])

    grid = {(x,y) : sign for x in range(w) for y in range(h) if (start := [start, (x,y)][(sign := data[y][x]) == "S"])}
    
    func = lambda x: next((z for z in x if z[0] not in seen), (0, "END", [], []))
    signs = {
        "|": lambda x, y: func((((x, y - 1), "|7FS", *(o := [[(x - 1, y)], [(x + 1, y)]])), ((x, y + 1), "|LJS", *o[::-1]))),
        "-": lambda x, y: func((((x + 1, y), "-J7S", *(o := [[(x, y - 1)], [(x, y + 1)]])), ((x - 1, y), "-LFS", *o[::-1]))),
        "L": lambda x, y: func((((x, y - 1), "|7FS", *(o := [[(x - 1, y), (x, y + 1)], []])), ((x + 1, y), "-J7S", *o[::-1]))),
        "J": lambda x, y: func((((x, y - 1), "|7FS", *(o := [[], [(x + 1, y), (x, y + 1)]])), ((x - 1, y), "-LFS", *o[::-1]))),
        "7": lambda x, y: func((((x - 1, y), "-LFS", *(o := [[], [(x, y - 1), (x + 1, y)]])), ((x, y + 1), "|LJS", *o[::-1]))),
        "F": lambda x, y: func((((x + 1, y), "-J7S", *(o := [[(x - 1, y), (x, y - 1)], []])), ((x, y + 1), "|LJS", *o[::-1]))),
    }

    s_x, s_y = start
    lefts, rights = set(), set()
    for next_value, valids in (((s_x + 1, s_y), "-J7S"), ((s_x - 1, s_y), "-LFS"), ((s_x, s_y + 1), "|LJS"), ((s_x, s_y - 1), "|7FS")):
        if (next_sign := grid.get(next_value, 0)) and next_sign in valids:
            seen, steps = {start}, 0
            while next_sign != "S" and (current_value := next_value) not in seen and (steps := steps + 1):
                seen.add(current_value)
                next_value, valids, left, right = signs[next_sign](*current_value)
                if (next_sign := grid.get(next_value, " ")) not in valids:
                    break
                for direction, collection in ((left, lefts), (right, rights)):
                    for x in direction:
                        if x in grid:
                            collection.add(x)
            print((steps - 1) // 2 + 1)
            break
    
    outer_coords = expand_collection({(x, y) for x in range(w) for y in range(h) if (x in [0, w - 1] or y in [0, h - 1]) and (x, y) not in seen})

    for inner_coords in [lefts - seen, rights - seen]:
        if inner_coords - outer_coords == inner_coords:
            print(len(expand_collection(inner_coords)))