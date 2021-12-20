with open('./20/input_a.txt') as f:
    enh = list(f.readline().strip())
    out = [list(a.strip()) for a in f if a.strip() != '']

def printgrid(grid: list): 
    for y in grid: print(''.join(y))
    
def enhance(pic : list, invert : bool):
    new = [['.' for a in range(len(pic)+2)] for a in range(len(pic)+2)]
    for x in range(len(new[0])): # calculate new value for neighbours
        for y in range(len(new)): 
            numb = ''
            for ny in range(y-1,y+2, 1): 
                for nx in range(x-1, x+2, 1): # get neighbours
                    if nx <1 or ny <1 or nx >=len(new)-1 or ny >=len(new)-1: numb += '0' if not invert else '1'
                    else: numb += '1' if pic[ny-1][nx-1] == '#' else '0'
            new[y][x] = enh[int(numb,2)] # lookup new value
    return new

steps = 2
for s in range(steps): out = enhance(out, s % 2 == 1)
s = sum([1 for a in out for b in a if b == '#'])
print(f'Part A: number of lit cells after {steps} steps - {s}')

steps = 48
for s in range(steps): out = enhance(out, s % 2 == 1)
s = sum([1 for a in out for b in a if b == '#'])
print(f'Part B: number of lit cells after {steps + 2} steps - {s}')