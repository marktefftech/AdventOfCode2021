<<<<<<< HEAD
from point2d import Point2D
=======
test = [0,1,2,3,4,5,6,7,8,9,10]

splitter = 5

print('len', len(test))
print('left', test[:splitter])
print('right', test[splitter+1:])
    
yo = 'YO'
no = 'NO'
>>>>>>> 370c5af1113e9de1dc9858fad1b5eb24d595fc95

def parse_input(input_lines: list[str]) -> dict[Point2D, int]:
    return {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input_lines)
        for x, weight in enumerate(line)
    }

<<<<<<< HEAD
input_lines = ['1234567346','12343256']

print(parse_input(input_lines))


visited: set[Point2D] = set()
visited.add(1)
print(visited)
=======
print(new)
>>>>>>> 370c5af1113e9de1dc9858fad1b5eb24d595fc95
