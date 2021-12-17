from point2d import Point2D

def parse_input(input_lines: list[str]) -> dict[Point2D, int]:
    return {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input_lines)
        for x, weight in enumerate(line)
    }

input_lines = ['1234567346','12343256']

print(parse_input(input_lines))


visited: set[Point2D] = set()
visited.add(1)
print(visited)
