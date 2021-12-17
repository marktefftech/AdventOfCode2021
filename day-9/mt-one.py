def populate():
    vals = []
    with open("/Users/mteffeteller/AoC2021/day-9/input.txt") as f:
        for row in f:
            data = list(map(int, row.strip()))
            vals.append(data)
    return vals

def checkLeft(vals,x,y):
    try:
        # don't want to set the pointer to -1
        if y == 0:
            return True
        diff = vals[x][y] - vals[x][y-1]
        return diff < 0
    except:
        return True

def checkRight(vals,x,y):
    try:
        if y == len(vals[0]):
            return True
        diff = vals[x][y] - vals[x][y+1]
        return diff < 0
    except:
        return True

def checkUp(vals,x,y):
    try:
        if x == 0:
            return True
        diff = vals[x][y] - vals[x-1][y]
        return diff < 0
    except:
        return True

def checkDown(vals,x,y):
    try:
        if x == len(vals):
            return True
        diff = vals[x][y] - vals[x+1][y]
        return diff < 0
    except:
        return True

def main():
    f = './input.txt'
    values = populate()
    
    lowPoints = []
    x,y = 0,0

    rowsChecked=0
    # Check every number in height map
    for x in range(len(values)):
        for y in range(len(values[0])):
            tempSum = []
            tempSum.append(checkLeft(values, x, y))
            tempSum.append(checkRight(values, x, y))
            tempSum.append(checkUp(values, x, y))
            tempSum.append(checkDown(values, x, y))
            if sum(tempSum) == 4:
                lowPoints.append(values[x][y])
        rowsChecked+=1

    print('checked %s rows' % rowsChecked)

    riskLevel = sum(lowPoints) + len(lowPoints)
    print('found %s low points' % (len(lowPoints)))    
    print('the risk level is %s' % (riskLevel))

main()