from collections import Counter

with open('./14/input_a.txt', 'r') as f:
    poly = f.readline().strip()
    mapping = dict([a.strip().split(' -> ') for a in f if a.strip() != ""])

def step(poly, mapping : dict, steps):
    for i in range(0,steps):
        print(f'Step - {i}')
        newpoly = ''
        for j in range(0,len(poly)-1):
            newpoly += poly[j] + mapping[poly[j:j+2]]
        poly = newpoly + poly[len(poly)-1]
    return poly

poly = step(poly, mapping, 10)
count = list(Counter(poly).values())
count.sort()
print(f'Part A: Poly after 10 iterations - {len(poly)}, diff = {count[len(count)-1] - count[0]}')

# To be rewritten for day 2... 