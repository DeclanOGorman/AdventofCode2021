with open('./1/input_a.txt', 'r') as f:
    input = [int(a.strip()) for a in f]

tot = sum([1 if input[a+1] > input[a] else 0 for a in range(0,len(input)-1)])
print(f'Part A: num descending = {tot}')

tot = sum([1 if input[a+1]+input[a+2]+input[a+3] > input[a]+input[a+1]+input[a+2] else 0 for a in range(0,len(input)-3)])
print(f'Part B: num sliding range descending = {tot}')