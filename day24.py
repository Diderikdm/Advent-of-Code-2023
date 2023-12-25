from itertools import combinations
import z3

det = lambda a, b: a[0] * b[1] - a[1] * b[0]

def find_intersection_point(line1, line2, rectangle_bounds, mx=800000000000000):
    px1, py1, vx1, vy1 = line1
    px2, py2, vx2, vy2 = line2
    xmin, ymin, xmax, ymax = rectangle_bounds
    px1_2 = px1 + vx1 * mx
    py1_2 = py1 + vy1 * mx
    px2_2 = px2 + vx2 * mx
    py2_2 = py2 + vy2 * mx
    xdiff = (px1 - px1_2, px2 - px2_2)
    ydiff = (py1 - py1_2, py2 - py2_2)
    div = det(xdiff, ydiff)
    if div:
        d = (det((px1, py1), (px1_2, py1_2)), det((px2, py2), (px2_2, py2_2)))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        if all([
            xmin <= x <= xmax, 
            ymin <= y <= ymax,
            max([px1, px1_2]) >= x >= min([px1, px1_2]),
            max([px2, px2_2]) >= x >= min([px2, px2_2]),
            max([py1, py1_2]) >= y >= min([py1, py1_2]), 
            max([py2, py2_2]) >= y >= min([py2, py2_2]),
        ]):
            return x, y
    
with open("day24.txt", "r") as file:
    data = file.read().splitlines()
    det = lambda a, b: a[0] * b[1] - a[1] * b[0]
    lines_x_y, lines_x_y_z = [], []
    p1 = 0
    for row in data:
        coords, velicities = row.split(" @ ")
        px, py, pz = [*map(int, coords.split(", "))]
        vx, vy, vz = [*map(int, velicities.split(", "))]
        lines_x_y.append((px, py, vx, vy))
        lines_x_y_z.append((px, py, pz, vx, vy, vz))
    for line1, line2 in combinations(lines_x_y, 2):
        if (point:= find_intersection_point(line1, line2, [200000000000000] * 2 + [400000000000000] * 2)):
            p1 += 1
    px, py, pz, vx, vy, vz = z3.Ints("px py pz vx vy vz")
    solver = z3.Solver()
    for e, line in enumerate(lines_x_y_z):
        ppx, ppy, ppz, vvx, vvy, vvz = line
        time = z3.Int(f"t{e}")
        solver.add(px + vx * time == ppx + vvx * time)
        solver.add(py + vy * time == ppy + vvy * time)
        solver.add(pz + vz * time == ppz + vvz * time)
    solver.check()
    print(p1, solver.model().evaluate(px + py + pz))