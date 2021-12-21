def foldUp(paper, foldLine):
    top = []
    bottom = []
    print('fold up')

    for i in range(len(paper)):
        if i < foldLine:
            top.append(paper[i])
        elif i == foldLine:
            continue
        else:
            bottom.append(paper[i])

    print('top')
    for i in top:
        print(i)
        print('\n')
        
    print('bottom')
    for i in bottom:
        print(i)
        print('\n')

    if len(bottom) > len(top):
        new  = bottom
        new.reverse()
        smaller = top
        smaller.reverse()
        
        for x in range(len(smaller)):
            for y in range(len(smaller[0])):
                if smaller[x][y] == 1:
                    new[-(x)-1][y] = 1

    else:
        new = top
        smaller = bottom
        #bottom.reverse()

        for x in range(len(smaller)):
            for y in range(len(smaller[0])):
                if smaller[x][y] == 1:
                    print(x,y)
                    new[-(x)-1][y] = 1

    return new

def foldLeft(paper, foldLine):
    left = []
    right = []

    for i in paper:
        left.append(i[:splitter])
        right.append(i[splitter+1:]) # do not include the fold line, there will be no dots on it

    print('left')
    for i in left:
        print(i)
        print('\n')
        
    print('right')
    for i in right:
        print(i)
        print('\n')

    if len(left[0]) < len(right[0]):
        smaller = left
        for item in right:
            item.reverse()
        new = right
        # for item in smaller:
        #     item.reverse()

        for row in range(len(smaller)):
            for col in range(len(smaller[0])):
                if smaller[row][col] == 1:
                    new[row][-(col)-1] = 1
        
    else:
        smaller = right
        new = left
        for row in range(len(smaller)):
            for col in range(len(smaller[0])):
                if smaller[row][col] == 1:
                    new[row][-(col)-1] = 1

    print('new')
    for i in new:
        print(i)
        print('\n')

    return new

def fillGrid(paper, dots):
    print('paper is %s rows and %s cols' % (len(paper), len(paper[0])))
    for dot in dots:
        # 1,0 
        paper[dot[1]][dot[0]] = 1
    
    return paper

###############################################
coords =  []
_x = []
_y = []
splitter=0

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
# switching x,y with h,w because of the way the coords are tracked in a grid
w = max(_x)+1 # zero indexing
h = max(_y)+1

G = [[0 for y in range(w)] for x in range(h)]

paper = fillGrid(G, coords)
print('paper')
for row in paper:
    print(row)
    print('\n')

print('now we need to fold at')
print(lvl, splitter)

if lvl == 'x':
    print('folding left at', splitter)
    ans = foldLeft(paper, splitter) 
else:
    ans = foldUp(paper, splitter)

print('ans')
for row in ans:
    print(row)
    print('\n')


dotties = 0

for x in range(len(ans)):
    for y in range(len(ans[0])):
        dotties+= ans[x][y]

print('Found %s dots' % (dotties))






