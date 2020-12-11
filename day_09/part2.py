import numpy as np


def check_number(target, prev):
    for a in prev:
        for b in prev:
            if a + b == target and a != b:
                return True
    return False


def find_contiguous_set(target_num):
    for size in range(2, len(numbers)):
        for pos in range(len(numbers)):
            contiguous_set = numbers[pos:pos + size]
            if sum(contiguous_set) == target_num:
                return min(contiguous_set) + max(contiguous_set)


numbers = np.array(open('input.txt').read().strip().split('\n'), dtype=int)
print(find_contiguous_set(133015568))