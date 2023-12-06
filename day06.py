def search(time, distance, low, high, low_high):
    while low < high:
        mid = (low + high) // 2
        if (time - mid) * mid > distance:
            low = mid + 1 if low_high else low
            high = high if low_high else mid
        else:
            low = low if low_high else mid + 1
            high = mid if low_high else high
    return low - low_high

with open("day06.txt") as file:
    data = file.read().splitlines()
    d1 = zip(*[[int(x) for x in y.split()[1:] if x] for y in data])
    d2 = [[int(''.join([x for x in y.split()[1:] if x])) for y in data]]
    for d in [d1, d2]:
        result = 1
        for time, distance in d:
            low = search(time, distance, 1, time // 2 + 1, 0)
            high = search(time, distance, time // 2 - 1, time - 1, 1)
            if low and high:
                result *= high - low + 1
        print(result)