import numpy as np

class point2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y

    def getCoordinates(self) -> np.array:
        return np.array([self.x, self.y])

    def translate(self, coordinates: np.array) -> None:
        self.x += coordinates.item(0)
        self.y += coordinates.item(1)

    def scale(self, constants: np.array) -> None:
        self.x *= constants.item(0)
        self.y *= constants.item(1)

    def rotateOrigin(self, angle: float) -> None:
        # bad bad bad bad. awful. assumes around origin
        self.x = (self.x * np.cos(np.radians(angle))) - (self.y * np.sin(np.radians(angle)))
        self.y = (self.x * np.sin(np.radians(angle))) + (self.y * np.cos(np.radians(angle)))


class line2D:
    def __init__(self, vertex0: point2D, vertex1: point2D) -> None:
        self.vertex0 = vertex0
        self.vertex1 = vertex1

    def getLength(self) -> float:
        return np.sqrt(((self.vertex0.getX - self.vertex1.getX)**2) + ((self.vertex0.getY - self.vertex1.getY)**2))

    def getEndpoints(self) -> np.array:
        return np.array([self.vertex0, self.vertex1])

    def getCoordinates(self) -> np.array: # 1:1 implementation of the exact algorithim on wikipedia #btw
        lineCoordinates = np.empty((0, 2))
        x0, y0 = self.vertex0
        x1, y1 = self.vertex1
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
            lineCoordinates = np.append(lineCoordinates, [[x0, y0]], axis = 0)
            e2 = error * 2
            if e2 >= dy:
                if x0 == x1:
                    return lineCoordinates
                error += dy
                x0 += sx
            if e2 <= dx:
                if y0 == y1:
                    return lineCoordinates
                error += dx
                y0 += sy


class point3D(point2D):
    def __init__(self, x: float, y: float, z: float) -> None:
        # initalizes the 3d point
        super().__init__(x, y)
        self.z = z

    def getZ(self) -> float:
        return self.z

    def getCoordinates(self) -> np.array:
        return np.append(super().getCoordinates(), self.z)

    def translate(self, coordinates: np.array) -> None:
        super().translate(coordinates)
        self.z += coordinates.item(2)

    def scale(self, constants: np.array) -> None:
        super().scale(constants)
        self.z *= constants.item(2)

    def rotateOrigin(self, angles: np.array) -> None:
        # oughhh... if the 2d one was awful, this is SUPER awful. assumes around origin
        angleX = np.radians(angles.item(0))
        angleY = np.radians(angles.item(1))
        angleY = np.radians(angles.item(2))

        temp = np.array([self.x, self.y, self.z])
        temp = temp @ np.array([1, 0, 0, 0],
                               [0, np.cos(angleX), np.sin(angleX), 0],
                               [0, -1 * np.sin(angleX), np.cos(angleX), 0]
                               [0, 0, 0, 1]) # rotate by x

        temp = temp @ np.array([np.cos(angleY), 0, -1 * np.sin(angleY), 0],
                               [0, 1, 0, 0],
                               [np.sin(angleY), 0, np.cos(angleY), 0],
                               [0, 0, 0, 1]) # rotate by y
        
        temp = temp @ np.array([np.cos(angleZ), np.sin(angleZ), 0, 0],
                               [-1 * np.sin(angleZ), np.cos(angleZ), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]) # last but not *z*east, rotate by z

        self.x = temp.item(0)
        self.y = temp.item(1)
        self.z = temp.item(2)

class line3D:
    def __init__(self, vertex0: point3D, vertex1: point3D) -> None:
        self.vertex0 = vertex0
        self.vertex1 = vertex1

    def getLength(self) -> float:
        return np.sqrt(((self.vertex0.getX - self.vertex1.getX)**2) + ((self.vertex0.getY - self.vertex1.getY)**2) + ((self.vertex0.getZ - self.vertex1.getZ)**2))

    def getEndpoints(self) -> np.array:
        return np.array([self.vertex0, self.vertex1])


class tri: # technically a subclass of point3D but there's really no point in inheriting it
    def __init__(self, vertex0: point3D, vertex1: point3D, vertex2: point3D) -> None:
        self.vertex0 = vertex0
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def getCoordinates(self) -> np.array:
        return np.array([self.vertex0.getCoordinates(), self.vertex1.getCoordinates(), self.vertex2.getCoordinates()])

    def getEdges(self) -> np.array:
        return np.array([line3D(self.vertex0.getCoordinates(), self.vertex1.getCoordinates()), 
        line3D(self.vertex1.getCoordinates(), self.vertex2.getCoordinates()), 
        line3D(self.vertex0.getCoordinates(), self.vertex2.getCoordinates())])

    def translate(self, coordinates: np.array) -> None:
        self.vertex0.translate(coordinates)
        self.vertex1.translate(coordinates)
        self.vertex2.translate(coordinates)

    def scale(self, constants: np.array) -> None:
        self.vertex0.scale(constants)
        self.vertex1.scale(constants)
        self.vertex2.scale(constants)

    def rotateOrigin(self, angles: np.array) -> None:
        self.vertex0.rotateOrigin(angles)
        self.vertex1.rotateOrigin(angles)
        self.vertex2.rotateOrigin(angles)

class model:
    def __init__(self, triArray: np.array) -> None: # input should be an array of tri objects
        self.triArray = triArray

    def getCoordinates(self) -> np.array:
        return np.array([tri.getCoordinates() for tri in triArray])

    def getEdges(self) -> np.array:
        return np.array([tri.getEdges() for tri in triArray])

    def translate(self, coordinates: np.array) -> None:
        return np.array([tri.translate(coordinates) for tri in triArray])

    def scale(self, constants: np.array) -> None:
        return np.array([tri.scale(constants) for tri in triArray])

    def rotateOrigin(self, angles: np.array) -> None:
        return np.array([tri.rotateOrigin(angles) for tri in triArray])

class Camera:
    def __init__(self, c: np.array, O: np.array, e: np.array):
        self.c = c
        self.O = O
        self.e = e

    def projection2D(self, a: np.array) -> np.array:
        d = np.identity(3)

        d = d @ np.array(
            [[1, 0, 0],
            [0, np.cos(np.radians(self.O.item(0))), np.sin(np.radians(self.O.item(0)))],
            [0, -1 * np.sin(np.radians(self.O.item(0))), np.cos(np.radians(self.O.item(0)))]]
        )

        d = d @ np.array(
            [[np.cos(np.radians(self.O.item(1))), 0, -1 * np.sin(np.radians(self.O.item(1)))],
            [0, 1, 0],
            [np.sin(np.radians(self.O.item(1))), 0, np.cos(np.radians(self.O.item(1)))]]
        )

        d = d @ np.array(
            [[np.cos(np.radians(self.O.item(2))), np.sin(np.radians(self.O.item(2))), 0],
            [-1 * np.sin(np.radians(self.O.item(2))), np.cos(np.radians(self.O.item(2))), 0],
            [0, 0, 1]]
        )

        d = d @ (a - self.c)

        return np.array([round(((self.e.item(2) * d.item(0)) / d.item(2)) + self.e.item(0)),
        round(((self.e.item(2) * d.item(1)) / d.item(2)) + self.e.item(1))])
            