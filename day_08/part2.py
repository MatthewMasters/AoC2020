
instructions = [ins.split(' ') for ins in open('input.txt').read().strip().split('\n')]

for idx, (cmd, val) in enumerate(instructions):
    changed_instructions = instructions.copy()

    changes = {'jmp' : 'nop', 'nop' : 'jmp', 'acc' : 'acc'}
    changed_instructions[idx] = [changes[cmd], val]

    seen = []
    idx = 0
    acc = []
    while idx not in seen:
        cmd, val = changed_instructions[idx]
        val = int(val)
        seen.append(idx)
        if cmd == 'jmp':
            idx += val
        else:
            idx += 1
            if cmd == 'acc':
                acc.append(val)

        if idx == len(changed_instructions):
            print(sum(acc))
            break
