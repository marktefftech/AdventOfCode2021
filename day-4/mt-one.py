import sys

class Board:
    def __init__(self):
        self.winner = False
        self.data = []
        rows,cols = 5,5
        self.tracker = [[0 for x in range(rows)] for y in range(cols)]

    def addRow(self, row):
        ints = [int(i) for i in row]
        self.data.append(ints)

    def updateTracker(self, x, y):
        self.tracker[x][y] = 1
        winnerByRow = self.checkRowForWin(x)
        winnerByCol = self.checkColumnForWin(y)

        if winnerByRow or winnerByCol:
            self.winner = True

    def checkRowForWin(self, x):
        tempSum = 0
        for i in self.tracker[x]:
            tempSum+=i
        return tempSum == 5

    def checkColumnForWin(self, y):
        tempSum = 0
        x = 0
        for i in self.tracker:
            tempSum+= self.tracker[x][y]
            x+=1
        return tempSum == 5

def populateBoards(f):
    boards = []
    board = Board()
    for l in f.readlines()[1:]:
        if l == '\n':
            boards.append(board)
            board = Board()
            continue
        board.addRow(l.strip().split())

    return boards

def checkBoardsForNumber(numberDrawn, boards):
    for board in boards:
        x,y = 0,0
        while x < 5:
            y=0
            while y < 5:
                if board.data[x][y] == numberDrawn:
                    board.updateTracker(x, y)
                    if board.winner:
                        print('we have a winner!')
                        print('lets check their score....')
                        calculateScore(board, numberDrawn)
                        break
                y+=1
            x+=1

# 1 0 1 0 1
# 0 1 1 1 1
# ...

# 5 5 7 2 7
# 1 7 2 6 7
# ...

# m = 
# u 
def calculateScore(board, n):
    marked, unmarked = [], []
    x, y = 0, 0

    while x < len(board.tracker):
        while y < len(board.tracker[0]):
            if board.tracker[x][y] == 0:
                unmarked.append(board.data[x][y])
            else:
                marked.append(board.data[x][y])
            y+=1
        y=0
        x+=1
    
    print('board: ' + str(board.data))
    print('tracker: ' + str(board.tracker))
    print('marked: ' + str(sum(marked)))
    print('unmarked: ' + str(sum(unmarked)))
    print('score is %s' % (n*sum(unmarked)))
    print('game over')
    sys.exit()

def main():
    infile = open('./input.txt', 'r')
    draws = [int(i) for i in infile.readline().split(',')]
    boards = populateBoards(infile) 

    # [1,9,5,6,7,2]
    for n in draws:
        checkBoardsForNumber(n, boards)

main()