

def parse_rules(filename):
    rule_text = open(filename).read().strip().split('\n')
    return dict([r.split(' bags contain ') for r in rule_text])


rules = parse_rules('input.txt')
queue = ['shiny gold']
seen = []
while len(queue):
    item = queue.pop(0)
    for key, val in rules.items():
        if key not in seen:
            if item in val:
                queue.append(key)
                seen.append(key)
print(len(seen))
