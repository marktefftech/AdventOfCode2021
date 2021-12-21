from point2d import Point2D

def parse_input(input_lines: list[str]) -> dict[Point2D, int]:
    return {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input_lines)
        for x, weight in enumerate(line)
    }

input_lines = ['1234567346','12343256']

weights = [{0,1},{0,2}]

if neighbor not in weights or neighbor in visited: