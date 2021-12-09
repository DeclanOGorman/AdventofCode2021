with open('./9/input_a.txt', 'r') as f:
    input = [list(map(int,list(a.strip()))) for a in f]

risk = 0; covered = list(); basins = list()
def basinSize(x,y):
    if [y,x] in covered or input[y][x] == 9: return 0 
    size = 0
    covered.append([y,x])
    if y > 0: size += basinSize(x,y-1)
    if y < len(input)-1: size += basinSize(x,y+1)
    if x > 0: size += basinSize(x-1,y)
    if x < len(input[0])-1: size += basinSize(x+1,y)
    return size + 1

for x in range (0, len(input[0])):
    for y in range(0, len(input)):
        basins.append(basinSize(x,y))
        if min(input[y-1][x] if y > 0 else 99,
            input[y+1][x] if y < len(input)-1 else 99,
            input[y][x-1] if x > 0 else 99,
            input[y][x+1] if x < len(input[0])-1 else 99 ) > input[y][x]:
            risk += input[y][x] + 1

basins.sort(reverse = 1)
print(f'Part A: Risk of lowest points - {risk}')
print(f'Part B: Largest basins - {basins[0]}, {basins[1]}, {basins[2]} - total = {basins[0]*basins[1]*basins[2]}')