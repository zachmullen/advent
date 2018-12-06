import itertools

lines = [l.split(', ') for l in open('input6.txt').readlines()]
pts = []
max_x, max_y = 0, 0
total = 0

for x, y in lines:
    x = int(x)
    y = int(y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    pts.append((x, y))

for gx, gy in itertools.product(range(max_x), range(max_y)):
    total_dist = 0
    for px, py in pts:
        total_dist += abs(px - gx) + abs(py - gy)
        if total_dist >= 10000:
            break
    else:
        total += 1
print(total)
