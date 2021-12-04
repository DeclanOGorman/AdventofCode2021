with open('./3/input_a.txt', 'r') as f:
    input_str = [a.strip() for a in f]
    input = [list(map(int, list(a))) for a in input_str]

ga = ''.join(['1' if a > len(input)/2 else '0' for a in [sum(a) for a in zip(*input)]])
eps = ''.join(['1' if a == '0' else '0' for a in list(ga)])
print(f'Part A: gamma - {ga} ({int(ga, 2)}), epsilon - {eps} ({int(eps,2)}), power - {int(ga,2) * int(eps,2)}') #3923414

ox = ''; co = ''
for i in range (0, len(ga)):
    ox += '1' if sum([int(a[i]) for a in input_str if a[:i] == ox])*2 >= len([a for a in input_str if a[:i] == ox]) else '0'
    if len([a for a in input_str if a[:i+1] == ox]) == 1:
        ox = [a for a in input_str if a[:i+1] == ox][0]
        break

for i in range (0, len(ga)):
    co += '0' if sum([1-int(a[i]) for a in input_str if a[:i] == co])*2 <= len([a for a in input_str if a[:i] == co]) else '1'
    if len([a for a in input_str if a[:i+1] == co]) == 1:
        co = [a for a in input_str if a[:i+1] == co][0]
        break

print(f'Part B: oxygen - {ox} ({int(ox, 2)}), CO2 - {co} ({int(co,2)}), life - {int(ox,2) * int(co,2)}')