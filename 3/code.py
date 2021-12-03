with open('./3/input_a.txt', 'r') as f:
    input = [list(map(int, a.split())) for a in f]

tots = list(map(sum, zip(*input)))
gamma = ''.join(['1' if a > len(input)/2 else '0' for a in tots])
eps = ''.join(['1' if a == '0' else '0' for a in list(gamma)])

print(f'Part A: gamma - {gamma} ({int(gamma, 2)}), epsilon - {eps} ({int(eps,2)})')
print(f'Part B: ')