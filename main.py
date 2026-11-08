import numpy as np

def projection2D(a: np.array, c: np.array, O: np.array, e: np.array) -> np.array:
    d = np.array(
        [[1, 0, 0],
        [0, np.cos(np.radians(O.item(0))), np.sin(np.radians(O.item(0)))],
        [0, -1 * np.sin(np.radians(O.item(0))), np.cos(np.radians(O.item(0)))]]
    )

    d *= np.array(
        [[np.cos(np.radians(O.item(1))), 0, -1 * np.sin(np.radians(O.item(1)))],
        [0, 1, 0],
        [np.sin(np.radians(O.item(1))), 0, np.cos(np.radians(O.item(1)))]]
    )

    d *= np.array(
        [[np.cos(np.radians(O.item(2))), np.sin(np.radians(O.item(2))), 0],
        [-1 * np.sin(np.radians(O.item(2))), np.cos(np.radians(O.item(2))), 0],
        [0, 0, 1]]
    )
    
    d *= (a - c)

    return np.array([((e.item(2) * d.item(0)) / d.item(2)) + e.item(0), 
    ((e.item(2) * d.item(1)) / d.item(2)) + e.item(1)])

def makeLine(pos0: np.array, pos1: np.array) -> np.array():
    lineCoordinates = np.array([])
    x0, y0 = pos0
    x1, y1 = pos1
    dx = abs(x1 - x0)

    if x0 < x1:
        sx = 1
    else:
        sx = -1

    dy = -abs(y1 - y0)

    if y0 < y1:
        sy = 1
    else:
        sy = -1

    error = dy + dx

    while True:
        lineCoordinates.append([x0, y0])
        if error * 2 >= dy:
            if x0 == x1:
                return lineCoordinates #TODO: FINISH THIS

def drawOut(a: np.array, width: int, height: int):
    screen = [["░░" for y in range(height)] for x in range(width)]

    for coordinate in a:
        screen[a.item(0)][a.item(1)] = "▓▓"

    for row in reversed(list(zip(*screen))):
        print("".join(row))