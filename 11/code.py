with open('./11/input_a.txt', 'r') as f:
    grid = [list(map(int, list(a.strip()))) for a in f]

def flash(grid,i,j):
    grid[i][j] = -1
    for x in range(i-1,i+2):
        for y in range(j-1,j+2): # iterate neighbours
            if x >= 0 and x < 10 and y >= 0 and y < 10 and grid[x][y] != -1: # only valid
                grid[x][y] = grid[x][y] + 1
                if grid[x][y] > 9: flash(grid, x, y) # recurse if flash triggered

totalFlashes, syncStep = 0, 0
for s in range(0, 1000):
    for i in range(0,10):
        for j in range(0,10):
            if grid[i][j] != -1: grid[i][j] = grid[i][j] + 1
            if grid[i][j] > 9:
                flash(grid, i, j)
    
    flashes = sum([1 if b == -1 else 0 for a in grid for b in a]) # count flashes
    grid = [[0 if b == -1 else b for b in a] for a in grid] # reset flashed to 0
    if s < 100: totalFlashes += flashes
    if flashes == 100: syncStep = s+1; break

print(f'Part A: Number of flashes after 100 steps - {flashes}') # test = 1656
print(f'Part B: Flashes sync at step - {syncStep}') # test = 195