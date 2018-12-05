import numpy as np

poly = np.array([ord(c) for c in open('input5.txt').read().strip()], dtype=np.int8)
min_ = len(poly)

for char in range(ord('a'), ord('z') + 1):
    without = poly[(poly != char) & (poly != char - 32)]
    while True:
        l = len(without)
        for i in range(l - 1):
            if abs(without[i] - without[i + 1]) == 32:
                without[i] = without[i + 1] = 0

        without = without[without != 0]
        if len(without) == l:
            break
    min_ = min(min_, len(without))
print(min_)
