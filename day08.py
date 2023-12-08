from copy import deepcopy

def recurse(keys, paths, start=0, cycle=1):
    if not keys:
        best.append(start)
        return
    for v in paths.pop(keys.pop(0)).values():
        for b in v.values():
            next_start, nxt, offset, cyc = start, [], b[0], b[1] - b[0]
            while (c := (next_start := next_start + cycle) % cyc not in (offset, offset % cyc)) or not nxt[1:]:
                if not c:
                    nxt.append(next_start)
            recurse(deepcopy(keys), deepcopy(paths), nxt[0], nxt[1] - nxt[0])
    return min(best)

with open("day08.txt", "r") as file:
    ins, data = file.read().split("\n\n")
    data = {x:tuple(y[1:-1].split(", ")) for x, y in [z.split(" = ") for z in data.splitlines()]}
    paths, best = {}, []
    for current in [k for k in data if k.endswith("A")]:
        e, paths[next_node := current] = -1, {}
        while True:
            if next_node.endswith("Z"):
                paths[current][next_node] = paths[current].get(next_node, {})
                paths[current][next_node][d] = paths[current][next_node].get(d := e % len(ins), []) + [e + 1]
                if all(all(len(x) > 1 for x in v.values()) for v in paths[current].values()):
                    break
            next_node = data[next_node][ins[(e := e + 1) % len(ins)] == "R"]
    print(f'p1: {min(sum(paths["AAA"]["ZZZ"].values(), []))}, p2: {recurse(list(paths.keys()), paths)}')