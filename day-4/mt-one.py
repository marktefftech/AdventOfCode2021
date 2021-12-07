from collections import defaultdict
# bingo = [7,4,9]

# boards =  [22,13,17,11,0] 
#           [8, 2, 23, 4,24]

# tracker = [[0,0,0,0,0],[0,0,0,0,0]

with open('./input.txt', 'r') as f:


    vals = f.read().splitlines()

    # ['1', '2', '3']
    instr = vals[0].split(',')
    boards = vals[1:]

    boardIdx = 0
    boardTracker = defaultdict(list)

    # {1: ['3','82']}
    for board in boards:
        if board == ' ':
            boardIdx+=1
            continue
        
        boardTracker[boardIdx] = boardTracker[boardIdx].append(board)
        

    print(instr)
    print(boards)
    print(boardTracker)

#def checkRow(row: list) -> int:


# for n in bingo:
#     row = 0
#     col = 0
#     for spot in boards[row]:
#         if spot == n:
#             print('number found')
#     row+=1

