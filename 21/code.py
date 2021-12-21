with open('./21/test_a.txt') as f:
    p1 = f.readline().strip()[-1:]
    p2 = f.readline().strip()[-1:]

ddice = 1
rolls = 0

def rollddice(num): 
    rolls += 1
    ddice = ddice + num
    return ddice * num - num

p1score, p2score = 0, 0
while max(p1score, p2score) < 1000:
    p1score += rollddice(3)
    if p1score >= 1000: break
    p2score += rollddice(3)
    if p2score >= 1000: break

print(f'Part A: score after first player reaches 1000 - {min(p1score, p2score)} x {rolls} = {min(p1score, p2score) * rolls}')