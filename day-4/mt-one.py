# 10,80,6,69,22,99,63,92,30,67,28,93,0,50,65,87,38,7,91,60,57,40,84,51,27,12,44,88,64,35,39,74,61,55,31,48,81,89,62,37,94,43,29,14,95,8,78,49,90,97,66,70,25,68,75,45,42,23,9,96,56,72,59,32,85,3,71,79,18,24,33,19,15,20,82,26,21,13,4,98,83,34,86,5,2,73,17,54,1,77,52,58,76,36,16,46,41,47,11,53

#  3 82 18 50 90
# 16 37 52 67 28
# 30 54 80 11 10
# 60 79  7 65 58
# 76 83 38 51  1

# 83 63 60 88 98
# 70 87  5 99 14
# 85  3 11 16 33
# 72 69 97 36 49
# 26 17 58 13  2

class Board:
    def __init__(self, _rows, _cols):
        x = _rows #[0,0,0,0,0]
        y = _cols
        board = [[0 for x in range(rows)] for y in range(cols)]

infile = open('./input.txt', 'r')

numbersDrawn = [int(i) for i in infile.readline().split(',')]

boards = [[]]

for l in infile[2:]:
    l.split('\n\n')
    print(l)


print(numbersDrawn)
# with open('./input.txt') as f:
#     boardIndex = 1
#     for row in f[2:]:
#         if l == '\n':
#             boardIndex+=1
#             continue
#         l = l.strip().split(' ')
#         # [3,83,18,50,90]
