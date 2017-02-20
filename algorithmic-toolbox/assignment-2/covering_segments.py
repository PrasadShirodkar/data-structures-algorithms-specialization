# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    # Sort the segments in non-decreasing order of right endpoint
    segments = sorted(segments, key = lambda x: x.end)

    segments1 = list()
    for s in segments:
        if len(points) == 0:
            points.append(s.end)
        elif s.start <= points[len(points) - 1] <= s.end:
            continue
        else:
            points.append(s.end)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p)
