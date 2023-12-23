from heapq import heapify, heappush, heappop

with open("day23.txt", "r") as file:
    data = file.read().splitlines()
    w = len(data[0]); h = len(data); result = []
    grid = {(x, y): data[y][x] for x in range(w) for y in range(h)}
    adj = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    conj = {k for k, v in grid.items() if v in "><v^." and sum(grid.get(x, "#") in "><v^." for x in adj(*k)) > 2} | {start := (1, 0), end := (w - 2, h - 1)}
    for i in range(2):
        conjunctions = {k : {} for k in conj}
        for k, v in conjunctions.items():
            heapify(queue := [(0, k, {k})])
            while queue:
                steps, current, seen = heappop(queue)
                if current in conjunctions and k != current: v[current] = min(v.get(current, 0), steps); continue
                for e, nxt in enumerate(adj(*current)):
                    new_steps = steps - 1
                    if nxt in grid and grid[nxt] != "#":
                        if not i and grid[nxt] in "><v^":
                            if (new_nxt := adj(*nxt)[e := "><v^".index(grid[nxt])]) == nxt: continue
                            new_steps -= 1; nxt = new_nxt
                        if nxt not in seen: heappush(queue, (new_steps, nxt, seen | {nxt}))
        heapify(queue := [(0, start, (start,))])
        r = 0; best = {}
        while queue:
            steps, current, seen = heappop(queue)
            for nxt, extra_steps in conjunctions[current].items():
                if nxt not in seen:
                    if (key := tuple(sorted(seen) + [nxt])) in best and best[key] <= steps: continue
                    best[key] = steps
                    if (new_steps := steps + extra_steps) and nxt == end: r = min(r, new_steps)
                    heappush(queue, (new_steps, nxt, key))
        result.append(-r)
    print(result)