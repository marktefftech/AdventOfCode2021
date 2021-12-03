class Position:

    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def forward(self, x):
        self.horizontal += x

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x

    def final(self):
        return self.horizontal * self.depth


inputs = open('input.txt', 'r').readlines()

submarine = Position()

for line in inputs:
    x, y = line.split()
    if x == "forward":
        submarine.forward(int(y))
    if x == "up":
        submarine.up(int(y))
    if x == "down":
        submarine.down(int(y))
print(submarine.final())