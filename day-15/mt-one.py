from queue import PriorityQueue, Queue

from point2d import Point2D

def dijkstra(weights: dict[Point2D, int], start: Point2D, end: Point2D,) -> int:
    visited: set[Point2D] = set()
    lowest_weights: dict[Point2D, int] = {}

    queue: Queue[tuple[int, Point2D]] = PriorityQueue()
    queue.put((0, start))
    while not queue.empty():
        # position with lowest weight from the start so far
        weight_from_start, pos = queue.get()
        if pos == end:
            # party time
            return weight_from_start

        # update neighbor weights
        x, y = pos
        for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if neighbor not in weights or neighbor in visited:
                # been there, done that
                continue

            new_weight = weight_from_start + weights[neighbor]
            old_weight = lowest_weights.get(neighbor)
            if old_weight and new_weight >= old_weight:
                # you can do better than that
                continue

            # found a more efficient route: update weight and add to queue
            lowest_weights[neighbor] = new_weight
            queue.put((new_weight, neighbor))

        visited.add(pos)

def parse_input(input_lines: list[str]) -> dict[Point2D, int]:
    return {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input_lines)
        for x, weight in enumerate(line)
    }

def part1(input_lines: list[str]) -> int:
    e = len(input_lines) - 1
    return dijkstra(
        weights=parse_input(input_lines),
        start=(0, 0),
        end=(e, e),
    )

lines=[]
with open('/Users/markteffeteller/dev/AdventOfCode2021/day-15/input.txt') as f:
    for line in f:
        lines.append(line.strip())#.strip().split())

weights = parse_input(lines)

print(part1(lines))