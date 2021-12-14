with open('/Users/mteffeteller/AoC2021/day-10/input.txt') as f:
    lines = []
    for l in f:
        data = list(l.strip())
        lines.append(data)

MATCHES = {')': '(', ']': '[', '}': '{', '>': '<'}
POINTSYSTEM = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}
part1_score = 0
              ^
for line in lines:
    # ['<([((<(<<{{{[{']
    stack = []
    for char in line:
        if char in MATCHES:
            # '{'
            opening = stack.pop()
            # '{' != '}'
            if opening != MATCHES[char]:
                # line is corrupted
                part1_score+= POINTSYSTEM[char]
                break
        else:
            stack.append(char)
    else:
       # Line isnt corrupt
       continue

print(part1_score) 


