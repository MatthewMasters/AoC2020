

def parse_rule(rule_text):
    outer_bag, inner_bags = rule_text.split(' bags contain ')
    inner_bags = [bag.replace(' bags', '').replace(' bag', '') for bag in inner_bags.replace('.', '').split(', ')]
    inner_bags = [(int(bag[0]), bag[2:]) if bag[0] != 'n' else (0, 'none') for bag in inner_bags]
    return outer_bag, inner_bags


def parse_rules(filename):
    rule_text = open(filename).read().strip().split('\n')
    return dict([parse_rule(r) for r in rule_text])


rules = parse_rules('input.txt')
queue = [['shiny gold', 1]]
seen = []
while len(queue):
    item, last_num = queue.pop(0)
    for key, val in rules.items():
        if item == key:
            for num, bag in val:
                queue.append([bag, last_num * num])
                seen.append(last_num * num)
print(sum(seen))