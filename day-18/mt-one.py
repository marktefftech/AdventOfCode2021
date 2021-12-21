import ast #abstract syntax tree

# [[[3,[8,6]],[6,1]],[[[1,1],2],[[1,0],0]]]
# [[[1,[7,3]],1],9]
lines = []
for line in open('/Users/markteffeteller/dev/AdventOfCode2021/day-18/test.txt','r'):
    line = ast.literal_eval(line.strip())
    lines.append(line)

def checkDepth(l):
    if isinstance(l, list):
        return 1 + max(checkDepth(item) for item in l)
    else :
        return 0


for i, line in enumerate(lines):
    try:
        print(i,line)
        combined = lines[i]
        next = lines[i+1]
        combined.append(next)
        print('combined')
        print(combined)
        print(checkDepth(combined))
    except:
        print('last line')

    # checkExplode(combined)
