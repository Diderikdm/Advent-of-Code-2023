from math import prod

def recurse(label, x, m, a, s):
    if label == "R": return 0
    if label == "A":
        for X, M, A, S in set(parts):
            if not (part := (X, M, A, S)) in p1 and all([q[0] <= Q <= q[1] for q, Q in ((x, X), (m, M), (a, A), (s, S))]):
                p1.add(part); parts.remove(part)
        return prod(len(range(i, j + 1)) for i, j in [x, m, a, s])
    
    result = 0
    for new_label, (X, M, A, S) in workflows[label]:
        new = [[max([q[0], Q[0]]), min([q[1], Q[1]])] for q, Q in [(x, X), (m, M), (a, A), (s, S)]]
        if not any(q[1] < q[0] for q in new):
            result += recurse(new_label, *new)
    return result

with open("day19.txt", "r") as file:
    data, parts = [x.splitlines() for x in file.read().split("\n\n")]
    parts = set(tuple(map(int, part.replace("{", "").replace("}", "").replace(",", "=").split("=")[1 : 8 : 2])) for part in parts)
    workflows, p1 = {}, set()
    for row in data:
        label, *checks = row.replace("}", "").replace("{", ",").split(",")
        workflows[label] = []
        vars = {**{x : 1 for x in "xmas"}, **{x : 4000 for x in "XMAS"}}
        for check in checks:
            if ":" not in check:  other_label, current = check, [[vars[x], vars[x.upper()]] for x in "xmas"]
            else:
                assertion, other_label = check.split(":")
                (var, value) = assertion.split(sign := ["<", ">"][">" in assertion])
                current = []
                for x in "xmas":
                    if x == var:
                        if   sign == ">": current += [[int(value) + 1, vars[x.upper()]]]; vars[x.upper()] = int(value)
                        elif sign == "<": current += [[vars[x], int(value) - 1]];         vars[x] = int(value)
                    else:                 current += [[vars[x], vars[x.upper()]]]                
            workflows[label].append((other_label, current))
    print([recurse("in", *[[1,4000]] * 4), sum(sum(x) for x in p1)][::-1])