import ast #abstract syntax tree
import itertools

# [[[3,[8,6]],[6,1]],[[[1,1],2],[[1,0],0]]]
# [[[1,[7,3]],1],9]
lines = []
for line in open('/Users/mteffeteller/AoC2021/day-18/test.txt','r'):
    line = ast.literal_eval(line.strip())
    lines.append(line)

def checkDepth(l):
    if isinstance(l, list):
        return 1 + max(checkDepth(item) for item in l)
    else :
        return 0

def explode(s):
    print('explode')
    print(s)
    for value in s:
            for subvalue in explode(value, tree_types):
                yield subvalue

for i, line in enumerate(lines):
    try:
        print(i,line)
        combined = lines[i]
        next = lines[i+1]
        combined.append(next)
        print('combined')
        print(checkDepth(combined))
        if checkDepth(combined) >= 0: 
            # found a 4-level nest, need to explode
            explode(combined)
    except:
        print('last line')

    # checkExplode(combined)
