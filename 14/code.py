from collections import Counter

with open('./14/input_a.txt', 'r') as f:
    poly = f.readline().strip()
    mapping = dict([a.strip().split(' -> ') for a in f if a.strip() != ""])

pairs = Counter([poly[i:i+2] for i in range(0, len(poly)-1)])
tally = Counter(list(poly))
results = list()

for i in range(0,40):
    for p, n in pairs.copy().items():
        c = mapping[p]
        tally[c] += n
        pairs[p] -= n
        pairs[p[0]+c] += n
        pairs[c+p[1]] += n
    hist = tally.most_common()
    results.append(hist[0][1] - hist[len(hist)-1][1])

print(f'Part A: Poly after 10 iterations, diff = {results[9]}') # test = 1588
print(f'Part B: Poly after 40 iterations, diff = {results[39]}')