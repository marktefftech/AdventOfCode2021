# cz-end
# cz-WR
# TD-end
from collections import defaultdict

d = defaultdict(list)

def countPaths(key, tree, goal, visited):
    # base case
    if key == goal:
        return 1

    total = 0
    # list of neighbor nodes
    for k in tree[key]:
        # if neighbor has been visited
        # this neighbor is lowercase and has already been visited, do not continue
        if k in visited:
            # next
            continue 

        if key.islower():
            newVisited = visited | {key}
        else:
            newVisited = visited

        total+=countPaths(k, tree, goal, newVisited)
    
    return total

for line in open('/Users/mteffeteller/AoC2021/day-12/input.txt', 'r'):
    a,b = line.strip().split('-')
    # {'kb': ['UM', 'cz', 'WR', 'TD', 'mj', 'start']...
    d[a].append(b)
    d[b].append(a)



print(countPaths("start", d, "end", set()))