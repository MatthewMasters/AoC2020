import numpy as np


def check_number(target, prev):
    for a in prev:
        for b in prev:
            if a + b == target and a != b:
                return True
    return False


numbers = np.array(open('input.txt').read().strip().split('\n'), dtype=int)
preamble_size = 25

for idx, num in enumerate(numbers[preamble_size:]):
    preamble = numbers[idx:idx+preamble_size]
    if not check_number(num, preamble):
        print(num)
        break
