with open('./13/input_a.txt', 'r') as f:
    input = [a.strip() for a in f if a.strip() != ""]

grid = [list(map(int,a.split(','))) for a in input if not a.startswith('fold')]
maxY = max([max(a[1],a[0]) for a in grid]) +1

def ghash(x, y): return y * maxY + x
def gunhash(hash): return [hash % maxY, int(hash/maxY)]

def fold(lgrid : dict, ins : list, start, num):
    for i in range(start, min(len(ins), num)):
        dir, line, newgrid = ins[i][0], ins[i][1], dict() 
        for p in lgrid:
            xy = gunhash(p)
            if dir == 'x' and xy[0] > line: 
                newgrid[ghash(line - (xy[0]-line), xy[1])] = 1
            elif dir == 'y' and xy[1] > line:
                newgrid[ghash(xy[0], line-(xy[1]-line))] = 1
            else:
                newgrid[p] = 1
        lgrid = newgrid
    return lgrid

gridDic = dict([[ghash(a[0],a[1]), 1] for a in grid])
ins = [['x' if 'x' in a else 'y', int(a.split('=')[1])] for a in input if a.startswith('fold')]

gridDic = fold(gridDic, ins, 0, 1)
print(f'Part A: number of dots after 1 fold - {len(gridDic)}') # test = 17

gridDic = fold(gridDic, ins, 1, 999)
x, y = max([gunhash(a)[0] for a in gridDic])+1, max([gunhash(a)[1] for a in gridDic])+1
img = [['.' for j in range(0, x)] for i in range(0, y)]
for g in gridDic: img[gunhash(g)[1]][gunhash(g)[0]] = '#'

print(f'Part B: number of dots after remaining folds - {len(gridDic)}, pattern:')
for r in img: print(''.join(r))