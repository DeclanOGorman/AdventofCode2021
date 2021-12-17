with open('./17/input_a.txt') as f: input = f.readline().strip()[15:].split(', y=')
targetx, targety = list(map(int,input[0].split('..'))), list(map(int,input[1].split('..')))

def fire(vel : list):
    height, pos = 0, [0,0]
    while pos[0] <= max(targetx) and pos[1] >= min(targety):
        if pos[0] >= min(targetx) and pos[1] <= max(targety): 
            return height
        pos[0] += vel[0]
        pos[1] += vel[1]
        height = max(height, pos[1])
        vel[0] = max(0,vel[0]-1)
        vel[1] -= 1
    return -999

vals = [fire([x,y]) for x in range(max(targetx)+1) for y in range(min(targety)-1, abs(min(targety))+1)]
vals = [a for a in vals if a > -999]
print(f'Part A/B: Max y velocity to hit target - height:{max(vals)} count:{len(vals)}')