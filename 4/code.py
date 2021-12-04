with open('./4/input_a.txt', 'r') as f:
    nums = f.readline().strip().split(',')
    f.readline
    input = [a.strip().split() for a in f]

boards = list(); board = list(); score = 0; winlist = list(); lastnum = 0
for a in input:
    if len(a) == 0:
        boards.append(board)
        boards.append(list(map(list, zip(*board))))
        board = list()
    else:
        board.append(a)
boards.append(board)
boards.append(list(map(list, zip(*board))))

for n in range(1,len(nums)):
    for b in boards:   
        if len([r for r in b if set(r).issubset(nums[:n])]) > 0: 
            if score == 0: score = sum([int(a) for r in b for a in r if a not in nums[:n]]) * int(nums[n-1])
            if int(boards.index(b)/2) not in winlist: 
                winlist.append(int(boards.index(b)/2))
                lastnum = n

print(f'Part A: score of first winning board - {score}')

score = sum([int(a) for r in boards[(winlist[len(winlist)-1])*2] for a in r if a not in nums[:lastnum]]) * int(nums[lastnum-1])
print(f'Part B: score of last winning board - {score}')