
def read_file(filename):
    return [text.split('\n') for text in open(filename).read().strip().split('\n\n')]


groups = read_file('input.txt')

count = 0
for group in groups:
    yeses = set.intersection(*[set(res) for res in group])
    count += len(yeses)

print(count)