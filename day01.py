with open("day01.txt") as file:
    numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    data = file.read().splitlines()
    r1, r2 = 0, 0
    for row in data:
        p1 = {e : x for e, x in enumerate(row) if x.isdigit()}
        p2 = {e : v for e, _ in enumerate(row) for k, v in numbers.items() if row[e:].startswith(k)}
        p2 = {**p1, **p2}
        r1 += int(p1[min(p1)] + p1[max(p1)])
        r2 += int(p2[min(p2)] + p2[max(p2)])
    print(f"p1: {r1}, p2: {r2}")
