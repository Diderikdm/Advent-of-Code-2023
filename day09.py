def recurse(row):
    if set(row) == {0}: return 0, 0
    left, right = recurse([row[e] - row[e-1] for e in range(1, len(row))])
    return row[0] - left, row[-1] + right

with open("day09.txt", "r") as file:
    data = [[*map(int, x.split())] for x in file.read().splitlines()]
    print([sum(x) for x in zip(*[*map(recurse, data)])][::-1])