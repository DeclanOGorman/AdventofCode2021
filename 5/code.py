with open('./5/input_a.txt', 'r') as f:
    vents = [list(map(int,a.strip().replace(' -> ',',').split(','))) for a in f]

size = max([max(a[0],a[2]) for a in vents])

def nav(input):
    grid = dict()
    for v in input:
        xstep = 1 if v[3]>v[1] else 0 if v[3]==v[1] else -1
        ystep = 1 if v[2]>v[0] else 0 if v[2]==v[0] else -1
        x = v[1]; y = v[0]
        grid[x*size + y] = 1 if x*size + y not in grid else grid[x*size + y] + 1
        while x != v[3] or y != v[2]:
            x += xstep; y += ystep
            grid[x*size + y] = 1 if x*size + y not in grid else grid[x*size + y] + 1
    return sum([1 if grid[a] > 1 else 0 for a in grid])

print(f'Part A: Number of overlapping grid points on H/Z lines - {nav([a for a in vents if a[0] == a[2] or a[1] == a[3]])}')
print(f'Part B: Number of overlapping grid points on all lines - {nav(vents)}')