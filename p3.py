import numpy as np

lines = open('input3.txt').readlines()
tw = th = 0
rects = []
for l in lines:
    id, _, corner, dim = l.rstrip().split()
    x, y = [int(v) for v in corner[:-1].split(',')]
    w, h = [int(v) for v in dim.split('x')]
    tw = max(tw, x + w)
    th = max(th, y + h)
    rects.append((x, y, x+w, y+h, id[1:]))

fabric = np.zeros((tw, th), dtype=np.uint16)
for x1, y1, x2, y2, _ in rects:
    fabric[x1:x2, y1:y2] += 1

for x, y, w, h, id in rects:
    if np.all(fabric[x1:x2, y1:y2] == 1):
        print(id)
        break
