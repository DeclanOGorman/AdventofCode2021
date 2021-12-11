with open('./10/input_a.txt', 'r') as f:
    input = [a.strip() for a in f]

syntaxScores = {')':3, ']':57, '}':1197, '>':25137}
completionScores = {'(':1, '[':2, '{':3, '<':4}

def check(line, stack):
    for c in line:
        if c in ['(','{','[','<']: stack.append(c)
        else: 
            p = stack.pop()
            if p != '(' and c == ')': return syntaxScores[c]
            elif p != '{' and c == '}': return syntaxScores[c]
            elif p != '[' and c == ']': return syntaxScores[c]
            elif p != '<' and c == '>': return syntaxScores[c]
    return 0

syntaxScore, completionScore = 0, list()
for a in input:
    stack = list()
    score = check(a, stack)
    if score > 0 or len(stack) == 0: syntaxScore += score
    else:
        stack.reverse()
        for i in stack: score = score * 5 + completionScores[i]
        completionScore.append(score)

completionScore.sort()
print(f'Part A: Syntax checker score - {syntaxScore}') #test = 26397
print(f'Part B: Median completion checker score - {completionScore[int(len(completionScore)/2)]}') #test = 288957