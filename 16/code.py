with open('./16/input_a.txt', 'r') as f: input = f.readline().strip()
versions = list()

def popper(list, num): return ''.join([list.pop(0) for _ in range(num)])
def parse(input : list):
    version = int(popper(input,3), 2)
    versions.append(version)
    type = int(popper(input,3),2)
    if type == 4: #literal
        end, num = False, ''
        while not end:
            end = True if popper(input, 1) == '0' else False
            num += popper(input, 4)
        return int(num,2)
    else: #operator
        lentype = popper(input,1)
        l = int(popper(input, 15 if lentype == '0' else 11),2)
        vals, prod = [], 1
        if lentype == '1': # num packets
            for _ in range(l): vals.append(parse(input))
        else: # num bits
            remaininglen = len(input) - l
            while len(input) > remaininglen: vals.append(parse(input))

        if type == 0: return sum(vals)
        if type == 1:
            for a in vals: prod = prod * a
            return prod
        if type == 2: return min(vals)
        if type == 3: return max(vals)
        if type == 5: return 1 if vals[0] > vals[1] else 0
        if type == 6: return 1 if vals[0] < vals[1] else 0
        if type == 7: return 1 if vals[0] == vals[1] else 0

bin_input = bin(int(input, 16))[2:].zfill(len(input)*4)
v = parse(list(bin_input))
print(f'Part A: Total sum version numbers - {sum(versions)}')
print(f'Part B: Value of the evaluated packet - {v}')