import numpy as np, math

def projection2D(a: np.array, c: np.array, O: np.array, e: np.array) -> tuple:
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

    return ((e.item(2) * d.item(0)) / d.item(2)) + e.item(0), 
    ((e.item(2) * d.item(1)) / d.item(2)) + e.item(1)