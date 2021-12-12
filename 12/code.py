with open('./12/input_a.txt', 'r') as f:
    input = [a.strip().split('-') for a in f]

caves = dict() # build bidirectional graph using dictionary
for a in input:
    if a[0] not in caves: caves[a[0]] = [a[1]]
    else: caves[a[0]].append(a[1])
    if a[1] not in caves: caves[a[1]] = [a[0]]
    else: caves[a[1]].append(a[0])

def nav(loc : str, path : list, doubled : bool = False): # Navigate
    if loc == 'end': return 1
    elif loc == 'start' and len(path) > 0: return 0 # End if start / finish reached
    elif str.islower(loc): # check small caves are not over-visited
        if doubled and loc in path: return 0
        elif loc in path: doubled = True
    path.append(loc)
    return sum([nav(i, path.copy(), doubled) for i in caves[loc]]) # evaulate children

print('Part A: Valid routes through caves with small caves visited once- {0}'.format(nav('start', list(), True)))
print('Part B: Valid routes through caves with 1st small cave visited twice - {0}'.format(nav('start', list())))