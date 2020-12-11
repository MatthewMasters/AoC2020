from collections import defaultdict
import numpy as np


jolts = sorted(np.array(open('input.txt').read().strip().split('\n'), dtype=int))
jolts = [0] + jolts + [max(jolts)+3]
print(jolts)

ways = defaultdict(int)
for value in jolts:
    ways[value] = sum(ways[value - delta] for delta in range(1, 4)) if value else 1
print(ways[jolts[-1]])
