import numpy as np


def read_map(filename):
    return np.array([[['.', '#'].index(c) for c in line.strip()] for line in open(filename).read().strip().split('\n')])


def count_trees(map, slope_x, slope_y):
    height, width = map.shape
    j = 0
    count = 0
    for i in range(0, height, slope_y):
        count += map[i, j]
        j += slope_x
        if j >= width:
            j -= width
    return count


map = read_map('input.txt')
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
answer = np.product([count_trees(map, *slope) for slope in slopes])
print(answer)