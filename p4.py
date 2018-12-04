from collections import defaultdict
import datetime
import numpy as np

AWAKE = 0
ASLEEP = 1
START = 2


class Event(object):
    def __init__(self, type, when, who):
        self.type = type
        self.when = when
        self.who = who


def get_event(l):
    date, time, msg = l.split(' ', 2)
    year, month, day = date[1:].split('-')
    hour, min = time[:-1].split(':')
    when = datetime.datetime(
        year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(min))
    who = None

    if msg.startswith('Guard'):
        type = START
        who = int(msg.split()[1][1:])
    elif msg.startswith('falls asleep'):
        type = ASLEEP
    else:
        type = AWAKE

    return Event(type=type, when=when, who=who)


counts = defaultdict(lambda: 0)
events = sorted((get_event(l) for l in open('input4.txt').readlines()), key=lambda e: e.when)
for e in events:
    if e.who is None:
        e.who = g
    else:
        g = e.who

    if e.type == ASLEEP:
        asleep = e.when
    elif e.type == AWAKE:
        counts[g] += (e.when - asleep).seconds / 60

guard = max(counts, key=counts.__getitem__)
minstogram = np.zeros((60,))
start = 0
for e in events:  # Find which minute the sleepy guard sleeps the most
    if e.who != guard:
        continue
    if e.type == ASLEEP:
        start = e.when.minute
    elif e.type == AWAKE:
        minstogram[start:e.when.minute] += 1

print(guard * np.argmax(minstogram))
