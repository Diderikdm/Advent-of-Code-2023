with open("day11.txt", "r") as file:
    data = file.read().splitlines()
    grid = {(x,y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "#"}
    horizontal = set(range(len(data[0]))) - {x for x, y in grid}
    vertical = set(range(len(data))) - {y for x, y in grid}
    s, s2 = 0, 0
    for galaxy in set(grid):
        grid.remove(galaxy)
        for other_galaxy in grid:
            left_h, right_h = sorted([galaxy[0], other_galaxy[0]])
            left_v, right_v = sorted([galaxy[1], other_galaxy[1]])
            sum_dist = right_h - left_h + right_v - left_v
            extra_h = sum(1 for x in horizontal if left_h < x < right_h)
            extra_v = sum(1 for x in vertical if left_v < x < right_v)
            s += sum_dist + (sum_extra := extra_h + extra_v)
            s2 += sum_dist + sum_extra * 999999
    print(s, s2)