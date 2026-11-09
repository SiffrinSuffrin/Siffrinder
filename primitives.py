import numpy as np

class point2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def getCoordinates(self) -> np.array:
        # self explanatory
        return np.array([self.x, self.y])

    def translate(self, coordinates: np.array) -> None:
        # self explanatory
        self.x += coordinates.item(0)
        self.y += coordinates.item(1)

    def scale(self, constants: np.array) -> None:
        # self explanatory
        self.x *= constants.item(0)
        self.y *= constants.item(1)

    def rotate(self, angle: int) -> None:
        # bad bad bad bad. awful. 
        self.x = (self.x * np.cos(np.radians(angle))) - (self.y * np.sin(np.radians(angle)))
        self.y = (self.x * np.sin(np.radians(angle))) + (self.y * np.cos(np.radians(angle)))


class point3D(point2D):
    def __init__(self, x: int, y: int, z: int) -> None:
        # initalizes the 3d point
        super().__init__(x, y)
        self.z = z

    def getCoordinates(self) -> np.array:
        # self explanatory
        return np.append(super().getCoordinates(), self.z)

    def translate(self, coordinates: np.array) -> None:
        # self explanatory
        super().translate(coordinates)
        self.z += coordinates.item(2)

    def scale(self, constants: np.array) -> None:
        # self explanatory
        super().scale(constants)
        self.z *= constants.item(2)

    def rotate(self, angles: np.array) -> None:
        # oughhh... if the 2d one was awful, this is SUPER awful
        temp = np.array([self.x, self.y, self.z])
        temp = temp @ np.array([1, 0, 0, 0],
                               [0, np.cos(np.radians(angles.item(0))), np.sin(np.radians(angles.item(0))), 0],
                               [0, -1 * np.sin(np.radians(angles.item(0))), np.cos(np.radians(angles.item(0))), 0]
                               [0, 0, 0, 1]) # rotate by x
        temp = temp @ np.array([],[],[],[]) # TODO: finish this


class tri: # technically a subclass of point3D but there's really no point in inheriting it
    def __init__(self, pos0: point3D, pos1: point3D, pos2: point3D) -> None:
        self.pos0 = pos0
        self.pos1 = pos1
        self.pos2 = pos2

    def getCoordinates(self) -> np.array:
        return np.array([self.pos0.getCoordinates(), self.pos1.getCoordinates(), self.pos2.getCoordinates()])

    def getEdges(self) -> np.array:
        return np.array([[self.pos0.getCoordinates(), self.pos1.getCoordinates()], 
        [self.pos1.getCoordinates(), self.pos2.getCoordinates()], 
        [self.pos0.getCoordinates(), self.pos2.getCoordinates()]])

    def translate(self, coordinates: np.array) -> None:
        self.pos0 = self.pos0.translate(coordinates)
        self.pos1 = self.pos1.translate(coordinates)
        self.pos2 = self.pos2.translate(coordinates)

    def scale(self, constants: np.array) -> None:
        self.pos0 = self.pos0.scale(constants)
        self.pos1 = self.pos1.scale(constants)
        self.pos2 = self.pos2.scale(constants)