def parse(E, S):
    data = []
    with open('/Users/mteffeteller/AoC2021/day-25/input.txt', 'r') as f:
        for line in f:
            data.append(line.strip().split())
    #print(data)
    for x in range(len(data)):
        for y in range(len(data[0])):
            #print(data[x][y])
            if data[x][y] == '>':
                # {(1,4): False}
                E[(x,y)] = False
            elif data[x][y] == 'v':
                # {(1,2): False}
                S[(x,y)] = False
            else:
                #data is a dot
                continue

# Initial state:
# ...>...
# .......
# ......>
# v.....>
# ......>
# .......
# ..vvv..

# After 1 step:
# ..vv>..
# .......
# >......
# v.....>
# >......
# .......
# ....v..


def main():
    E = {}
    S = {}
    data = parse(E, S)

    print(E)
    print(S)

if __name__ == "__main__":
    main()