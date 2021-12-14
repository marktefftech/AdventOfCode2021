# HOSBSKBBBFSPPPCCCHN

# KO -> H
# OK -> P
# BO -> C

from collections import defaultdict, Counter

pairs = defaultdict(str)

with open('/Users/markteffeteller/dev/AdventOfCode2021/day-14/input.txt', 'r') as f:
    lines = f.readlines()
    polymer = lines[0].strip()
    print('original polymer')
    print(polymer)

    for line in lines[2:]:
        key, val = line.strip().split(' -> ')
        
        pairs[key] = val

def grow(s, d):
    new = ''
    # LSFNSKJDFNSDJ
    i = 0
    #print(s)
    s = list(s)
    for currentLetter in s:
        if i+1 >= len(list(s)):
            new+=currentLetter
            continue
        
        n = s[i+1]

        pair = currentLetter+n

        if pair in d:
            new+=currentLetter
            new+=d[pair] 
            # print('new')
            # print(new)       
            i+=1
        else:
            print('not found')
            new+=c
            i+=1
            continue
    return new


c=0

while c < 10:

    polymer = grow(polymer, pairs)
    c+=1

ans = Counter(list(polymer))
print(polymer)
print('polymer after %s rounds' % c)
print(ans)
print(max(ans.values()) - min(ans.values()))
