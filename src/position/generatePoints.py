from typing import List
from src.position.position import Position


def generatePoints(positions, precision) -> List:
    pointList = []
    length = len(positions)
    for i in range(0, length - 1):
        rangeX = positions[i + 1].x - positions[i].x
        rangeY = positions[i + 1].y - positions[i].y
        for j in range(0, precision + 1):
            pointList.append(
                Position(j * rangeX / precision + positions[i].x,
                         j * rangeY / precision + positions[i].y))
    return pointList


if __name__ == '__main__':
    POINTS = [
        Position(0.2, 0.2),
        Position(0.2, 0.8),
        Position(0.8, 0.8),
        Position(0.8, 0.2)
    ]

    PRECISION = 10
    pointList = generatePoints(POINTS, PRECISION)
    for point in pointList:
        print("{} ; {} - ".format(point.x, point.y))