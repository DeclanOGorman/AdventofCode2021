with open('./2/input_a.txt', 'r') as f:
    input = [a.split() for a in f]

fwd = 0; dep = 0; aim = 0
for a in input:
    dir = int(a[1])
    if a[0] == 'forward':
        fwd += dir
        dep += dir * aim
    else:
        aim += dir if a[0] == 'down' else dir*-1 

print(f'Part A: Forwards - {fwd}, Depth - {aim}, Answer - {fwd * aim}')
print(f'Part B: Forwards - {fwd}, Depth - {dep}, aim - {aim} Answer - {fwd * dep}')