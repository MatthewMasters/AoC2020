

def check_validity(password):
    rule, text = password.split(":")
    rule_pos, rule_let = rule.split(' ')
    pos_a, pos_b = [int(pos) for pos in rule_pos.split('-')]
    condition_a = text[pos_a] == rule_let
    condition_b = text[pos_b] == rule_let
    return (condition_a or condition_b) and not (condition_a and condition_b)


def count_valid(passwords):
    return sum([check_validity(password) for password in passwords])


def read_passwords(filename):
    return open(filename).read().strip().split('\n')


passwords = read_passwords('input.txt')
print(count_valid(passwords))