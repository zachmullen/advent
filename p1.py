import itertools

vals = [int(v) for v in open('input1.txt').readlines()]
cur = 0
freqs = {cur}
for v in itertools.cycle(vals):
    cur += v
    if cur in freqs:
        print(cur)
        break
    freqs.add(cur)
