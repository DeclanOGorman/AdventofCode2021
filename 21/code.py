
with open('./21/input_a.txt') as f:
    p1 = int(f.readline().strip()[-1:])
    p2 = int(f.readline().strip()[-1:])

ddice = 1
def rollddice(num): 
    global ddice
    ddice += num
    return (ddice-1) * num - num

p1score, p1loc, p2score, p2loc = 0, p1, 0, p2
while max(p1score, p2score) < 1000:
    p1loc = (((p1loc + rollddice(3))-1) %10) +1
    p1score += p1loc
    if p1score >= 1000: break
    p2loc = (((p2loc + rollddice(3))-1) %10) +1
    p2score += p2loc
    if p2score >= 1000: break

print(f'Part A: score after first player reaches 1000 - {min(p1score, p2score)} x {ddice-1} = {min(p1score, p2score) * ddice-1}')