import statistics
with open('./7/input_a.txt', 'r') as f:
    input = list(map(int,f.readline().strip().split(',')))

fuel = sum([abs(a - int(statistics.median(input))) for a in input])
print(f'Part A: fuel cost to align (fixed cost / median) - {fuel}')

fuel = 9999999999
for i in range(min(input), max(input)):
    fuel = int(min(fuel, sum([abs(a - i)*(abs(a - i)+1)/2 for a in input])))
print(f'Part B: fuel cost to align (increasing costs) - {fuel}')