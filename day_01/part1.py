import itertools
import numpy as np


def solution(instructions, n):
    for pair in itertools.permutations(instructions, n):
        if sum(pair) == 2020:
            return np.product(pair)


def read_list(filename):
    return map(int, open(filename).read().strip().split('\n'))


instructions = read_list("input.txt")
print(solution(instructions, 2))