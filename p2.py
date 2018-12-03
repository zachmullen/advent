ids = open('input2.txt').read().split()

for i, left in enumerate(ids):
    for right in ids[i+1:]:
        diffs = pos = 0
        for p, (lc, rc) in enumerate(zip(left, right)):
            if lc != rc:
                diffs += 1
                pos = p
            if diffs > 1:
                break
        if diffs == 1:
            print(left[:pos] + left[pos+1:])
            break
