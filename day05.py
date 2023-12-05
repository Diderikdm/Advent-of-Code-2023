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
                    start, end = current_ranges.pop(0)
                    for destination, source, rng in arrangements:
                        if source <= start and source + rng > start:
                            if end - start < rng:
                                next_ranges.append((destination + (start - source), destination + (end - source)))
                            else:
                                next_ranges.append((destination + (start - source), destination + (start + rng - 1 - source)))
                                current_ranges.append((start + rng, end))
                        elif source <= end and source + rng > end:
                            next_ranges.append((destination, destination + (end - source - 1)))
                            current_ranges.append((start, source - 1))
                        elif source > start and source + rng < end:
                            next_ranges.append((destination, destination + rng - 1))
                            current_ranges.extend([(start, source - 1), (source + rng, end)])
                        else:
                            continue
                        break
                    else:
                        next_ranges.append((start, end))
                current_ranges = next_ranges
            mins.append((min(x[0] for x in current_ranges)))
        result.append(min(mins))
    print("p1: {}, p2: {}".format(*result))