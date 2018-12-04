from collections import defaultdict
import datetime
import numpy as np


class Event(object):
    def __init__(self, l):
        date, time, msg = l.split(' ', 2)
        y, M, d = (int(v) for v in date[1:].split('-'))
        h, m = (int(v) for v in time[:-1].split(':'))
        self.type = 'wake'
        self.when = datetime.datetime(year=y, month=M, day=d, hour=h, minute=m)
        self.who = None

        if msg.startswith('Guard'):
            self.type = 'start'
            self.who = int(msg.split()[1][1:])
        elif msg.startswith('falls asleep'):
            self.type = 'sleep'


counts = defaultdict(lambda: 0)
events = sorted((Event(l) for l in open('input4.txt').readlines()), key=lambda e: e.when)
for e in events:
    if e.who is None:
        e.who = g
    else:
        g = e.who
    if e.type == 'sleep':
        asleep = e.when
    elif e.type == 'wake':
        counts[g] += (e.when - asleep).seconds / 60

minstogram = np.zeros((len(counts), 60), dtype=np.uint16)
keys = {k: i for i, k in enumerate(counts)}
for e in events:
    if e.type == 'sleep':
        start = e.when.minute
    elif e.type == 'wake':
        minstogram[keys[e.who], start:e.when.minute] += 1

guard, minute = np.unravel_index(minstogram.argmax(), minstogram.shape)
for g, i in keys.items():
    if i == guard:
        break
print(minute * g)
