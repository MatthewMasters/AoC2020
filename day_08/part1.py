
instructions = [ins.split(' ') for ins in open('input.txt').read().strip().split('\n')]

seen = []
idx = 0
acc = []
while idx not in seen:
    cmd, val = instructions[idx]
    val = int(val)
    seen.append(idx)
    if cmd == 'jmp':
        idx += val
    else:
        idx += 1
        if cmd == 'acc':
            acc.append(val)

print(sum(acc))