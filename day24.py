from itertools import combinations
import z3

def find_intersection_point(px1, py1, vx1, vy1, px2, py2, vx2, vy2, xmin, ymin, xmax, ymax, mx=800000000000000):
    det = lambda a, b: a[0] * b[1] - a[1] * b[0]
    xdiff = (px1 - (px1_2 := px1 + vx1 * mx), px2 - (px2_2 := px2 + vx2 * mx))
    ydiff = (py1 - (py1_2 := py1 + vy1 * mx), py2 - (py2_2 := py2 + vy2 * mx))
    if (div := det(xdiff, ydiff)):
        d = (det((px1, py1), (px1_2, py1_2)), det((px2, py2), (px2_2, py2_2)))
        x, y = [det(d, diff) / div for diff in [xdiff, ydiff]]
        if xmin <= x <= xmax and ymin <= y <= ymax and all((min([a, b]) <= c <= max([a, b])) for a, b, c in ((px1, px1_2, x), (px2, px2_2, x), (py1, py1_2, y), (py2, py2_2, y))):
            return x, y
    
with open("day24.txt", "r") as file:
    data = file.read().splitlines()
    lines_x_y = []
    p1 = 0
    solver = z3.Solver()
    pxu, pyu, pzu, vxu, vyu, vzu = z3.Ints("pxu pyu pzu vxu vyu vzu")
    for e, row in enumerate(data):
        px, py, pz, vx, vy, vz = [*map(int, row.replace(" @ ", ", ").split(", "))]
        lines_x_y.append((px, py, vx, vy))
        time = z3.Int(f"t{e}")
        solver.add(pxu + vxu * time == px + vx * time)
        solver.add(pyu + vyu * time == py + vy * time)
        solver.add(pzu + vzu * time == pz + vz * time)
    for line1, line2 in combinations(lines_x_y, 2):
        if (point:= find_intersection_point(*line1, *line2, *[200000000000000] * 2 + [400000000000000] * 2)):
            p1 += 1
    solver.check()
    print(p1, solver.model().evaluate(pxu + pyu + pzu))