with open('./6/input_a.txt', 'r') as f:
    input = list(map(int,f.readline().strip().split(',')))

fish = list([0,0,0,0,0,0,0,0,0])
for i in range(0,8):
    fish[i] = sum([1 for a in input if a == i])

def observe(days):
    for d in range(0,days):
        newfish = fish[0]
        for i in range(0,8): 
            fish[i] = fish[i+1] + (newfish if i == 6 else 0)
        fish[8] = newfish
    return sum([a for a in fish])

print(f'Part A: after 80 days {observe(80)} lanternfish remaining')
print(f'Part B: after 256 days {observe(256-80)} lanternfish remaining')