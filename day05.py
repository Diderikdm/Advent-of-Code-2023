with open("day05.txt") as file:
    data = file.read().split("\n\n")
    seeds = [int(x) for x in data.pop(0).split()[1:]]
    result, mins = [], []
    for s in [[[x, x] for x in seeds], [[seeds[e], seeds[e] + seeds[e + 1] - 1] for e in range(0, len(seeds), 2)]]:
        for seed_min, seed_max in s:
            current_ranges = [(seed_min, seed_max)]
            for block in data:
                arrangements = [[int(x) for x in y.split()] for y in block.splitlines()[1:]]
                next_ranges = []
                while current_ranges:
                    current_start, current_end = current_ranges.pop(0)
                    for destination, source, r in arrangements:
                        if source <= current_start and source + r > current_start:
                            if current_end - current_start < r:
                                next_ranges.append((destination + (current_start - source), destination + (current_end - source)))
                            else:
                                next_ranges.append((destination + (current_start - source), destination + (current_start + r - 1 - source)))
                                current_ranges.append((current_start + r, current_end))
                        elif source <= current_end and source + r > current_end:
                            next_ranges.append((destination, destination + (current_end - source - 1)))
                            current_ranges.append((current_start, source - 1))
                        elif source > current_start and source + r < current_end:
                            next_ranges.append((destination, destination + r - 1))
                            current_ranges.extend([(current_start, source - 1), (source + r, current_end)])
                        else:
                            continue
                        break
                    else:
                        next_ranges.append((current_start, current_end))
                current_ranges = next_ranges
            mins.append((min(x[0] for x in current_ranges)))
        result.append(min(mins))
    print("p1: {}, p2: {}".format(*result))