

def check_validity(password):
    rule, text = password.split(":")
    rule_range, rule_let = rule.split(' ')
    rule_min, rule_max = rule_range.split('-')
    return int(rule_min) <= text.count(rule_let) <= int(rule_max)


def count_valid(passwords):
    return sum([check_validity(password) for password in passwords])


def read_passwords(filename):
    return open(filename).read().strip().split('\n')


passwords = read_passwords('input.txt')
print(count_valid(passwords))