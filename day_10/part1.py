import numpy as np


jolts = sorted(np.array(open('input.txt').read().strip().split('\n'), dtype=int))
jolts.append(max(jolts)+3)

last = 0
deltas = []
for n in jolts:
    delta = n - last
    deltas.append(delta)
    last = n

print(np.product(np.unique(deltas, return_counts=True)[1]))