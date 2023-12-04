with open("day03.txt") as file:
    data = file.read().splitlines()
    adj = lambda x, y: ((x+1, y), (x+1, y+1), (x+1, y-1), (x-1, y), (x-1, y+1), (x-1, y-1), (x, y+1), (x, y-1))
    seen = set()
    r1, r2 = 0, 0
    grid = {(x, y) : data[y][x] for x in range(len(data[0])) for y in range(len(data))}
    for k, v in grid.items():
        if not v.isdigit() and not v == "." and not (p2_adj := []):
            for other in adj(*k):
                if other in grid and other not in seen and grid[other].isdigit():
                    current_numbers = {other}
                    for next_coord, direction in [(other, 1), (other, -1)]:
                        while (next_coord := (next_coord[0] + direction, next_coord[1])) in grid and grid[next_coord].isdigit():
                            current_numbers.add(next_coord)
                    r1 += (number := int(''.join([grid[x] for x in sorted(current_numbers)])))
                    p2_adj.append(number)
                    seen |= current_numbers
            if v == "*" and len(p2_adj) == 2:
                r2 += p2_adj[0] * p2_adj[1]
    print(f"p1: {r1}, p2: {r2}")
