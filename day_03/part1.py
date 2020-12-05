import numpy as np


def read_map(filename):
    return np.array([[['.', '#'].index(c) for c in line.strip()] for line in open(filename).read().strip().split('\n')])


def count_trees(map, slope):
    height, width = map.shape
    j = 0
    count = 0
    for i in range(1, height):
        j += slope
        if j >= width:
            j -= width
        count += map[i, j]
    return count


map = read_map('input.txt')
print(count_trees(map, 3))