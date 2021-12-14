# 654,548
# 393,737
# ...
# fold along x=655

coords = []
_x = []
_y = []

def foldLeft(paper, splitter):
    left = []
    right = []
    splitter = (len(paper[0])/2)

    for i in paper:
        left.append(i[:splitter])
        right.append(i[splitter+1:])
    
    print(len(left))
    print(len(right))
    print(len(left[0]))
    print(len(right[0]))

    for x in range(len(left)):
        for y in range(len(left[0])-1):
            if left[x][y] == 1  or right[x][y] == 1:
                left[x][y] = 1
            else:
                0

    return left

def foldUp(paper, splitter):
    top = paper[0:splitter]
    print('top length',len(top))
    bottom = paper[splitter:]
    
    for x, y in top:
        for f, b in bottom:
            top[x][y] = 1 if bottom[f][b] == 1 or top[x][y] == 1 else 0

    return top

def fillGrid(paper, dots):
    # [6,8]
    print('paper is %s rows and %s cols' % (len(paper), len(paper[0])))
    for dot in dots:
        paper[dot[0]][dot[1]] = 1
    
    return paper

for line in open('/Users/mteffeteller/AoC2021/day-13/input.txt', 'r'):
    if line.strip().split(' ')[0] == 'fold':
        instructions = line.strip().split(' ')
        s = instructions[2]
        lvl, val = s.split('=')
        splitter = int(val)
        break

    elif line == '\n':
        continue

    else:
        x,y = line.strip().split(',')
        coords.append([int(x), int(y)])
        _x.append(int(x))
        _y.append(int(y))

# coords = [[2,4], [6,8]]
r = max(_x)+1
c = max(_y)+1

G = [[0 for y in range(c)] for x in range(r)]

paper = fillGrid(G, coords)

if lvl == 'x':
    print('folding left at', splitter)
    ans = foldLeft(paper, splitter) 
else:
    ans = foldUp(paper, splitter)

dotties = 0

for x in range(len(ans)):
    for y in range(len(ans[0])):
        dotties+= ans[x][y]

print('Found %s dots' % (dotties))
