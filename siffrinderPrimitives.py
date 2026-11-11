import numpy as np, os

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
        tempX = (self.x * np.cos(np.radians(angle))) - (self.y * np.sin(np.radians(angle)))
        self.y = (self.x * np.sin(np.radians(angle))) + (self.y * np.cos(np.radians(angle)))
        self.x = tempX


class line2D:
    def __init__(self, vertex0: point2D, vertex1: point2D) -> None:
        self.vertex0 = vertex0
        self.vertex1 = vertex1

    def getLength(self) -> float:
        return np.sqrt(((self.vertex0.getX() - self.vertex1.getX())**2) + ((self.vertex0.getY() - self.vertex1.getY())**2))

    def getEndpoints(self) -> np.array:
        return np.array([self.vertex0, self.vertex1])

    def getCoordinates(self) -> np.array: # 1:1 implementation of the exact algorithim on wikipedia #btw
        lineCoordinates = np.array([])
        x0, y0 = self.vertex0.getCoordinates()
        x1, y1 = self.vertex1.getCoordinates()
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
            lineCoordinates = np.append(lineCoordinates, point2D(x0, y0))
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
        angleZ = np.radians(angles.item(2))

        temp = np.array([self.x, self.y, self.z])
        temp = temp @ np.array([[1, 0, 0],
                                [0, np.cos(angleX), np.sin(angleX)],
                                [0, -1 * np.sin(angleX), np.cos(angleX)]]) # rotate by x

        temp = temp @ np.array([[np.cos(angleY), 0, -1 * np.sin(angleY)],
                                [0, 1, 0],
                                [np.sin(angleY), 0, np.cos(angleY)]]) # rotate by y
        
        temp = temp @ np.array([[np.cos(angleZ), np.sin(angleZ), 0],
                                [-1 * np.sin(angleZ), np.cos(angleZ), 0],
                                [0, 0, 1]]) # last but not *z*east, rotate by z

        self.x = temp.item(0)
        self.y = temp.item(1)
        self.z = temp.item(2)

class line3D:
    def __init__(self, vertex0: point3D, vertex1: point3D) -> None:
        self.vertex0 = vertex0
        self.vertex1 = vertex1

    def getLength(self) -> float:
        return np.sqrt(((self.vertex0.getX() - self.vertex1.getX())**2) + ((self.vertex0.getY() - self.vertex1.getY())**2) + ((self.vertex0.getZ() - self.vertex1.getZ())**2))

    def getEndpoints(self) -> np.array:
        return np.array([self.vertex0, self.vertex1])


class tri: # technically a subclass of point3D but there's really no point in inheriting it
    def __init__(self, vertex0: point3D, vertex1: point3D, vertex2: point3D, shading: str) -> None:
        self.vertex0 = vertex0
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.shading = shading

    def getCoordinates(self) -> np.array:
        return np.array([self.vertex0.getCoordinates(), self.vertex1.getCoordinates(), self.vertex2.getCoordinates()])

    def getEdges(self) -> np.array:
        return np.array([line3D(self.vertex0, self.vertex1), 
        line3D(self.vertex1, self.vertex2), 
        line3D(self.vertex0, self.vertex2)])

    def getShading(self) -> str:
        return self.shading

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

    def getTri(self) -> np.array:
        return self.triArray

    def getCoordinates(self) -> np.array:
        return np.array([tri.getCoordinates() for tri in self.triArray])

    def getEdges(self) -> np.array:
        return np.array([tri.getEdges() for tri in self.triArray])

    def translate(self, coordinates: np.array) -> None:
        return np.array([tri.translate(coordinates) for tri in self.triArray])

    def scale(self, constants: np.array) -> None:
        return np.array([tri.scale(constants) for tri in self.triArray])

    def rotateOrigin(self, angles: np.array) -> None:
        return np.array([tri.rotateOrigin(angles) for tri in self.triArray])

class camera:
    def __init__(self, cameraCoordinates: np.array, angles: np.array, displayCoordinates: np.array) -> None:
        self.cameraCoordinates = cameraCoordinates
        self.angles = angles
        self.displayCoordinates = displayCoordinates

    def projection2D(self, a: np.array) -> tuple:
        cameraTransform = np.identity(3)

        cameraTransform = cameraTransform @ np.array(
            [[1, 0, 0],
            [0, np.cos(np.radians(self.angles.item(0))), np.sin(np.radians(self.angles.item(0)))],
            [0, -1 * np.sin(np.radians(self.angles.item(0))), np.cos(np.radians(self.angles.item(0)))]]
        )

        cameraTransform = cameraTransform @ np.array(
            [[np.cos(np.radians(self.angles.item(1))), 0, -1 * np.sin(np.radians(self.angles.item(1)))],
            [0, 1, 0],
            [np.sin(np.radians(self.angles.item(1))), 0, np.cos(np.radians(self.angles.item(1)))]]
        )

        cameraTransform = cameraTransform @ np.array(
            [[np.cos(np.radians(self.angles.item(2))), np.sin(np.radians(self.angles.item(2))), 0],
            [-1 * np.sin(np.radians(self.angles.item(2))), np.cos(np.radians(self.angles.item(2))), 0],
            [0, 0, 1]]
        )

        cameraTransform = cameraTransform @ (a - self.cameraCoordinates)

        return np.array([round(((self.displayCoordinates.item(2) * cameraTransform.item(0)) / cameraTransform.item(2)) + self.displayCoordinates.item(0)),
        round(((self.displayCoordinates.item(2) * cameraTransform.item(1)) / cameraTransform.item(2)) + self.displayCoordinates.item(1))]), cameraTransform.item(2)

class screen:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.frame = np.array([])
        self.depth = np.array([])

    def newFrame(self) -> None:
        self.frame = np.array([["  " for y in range(self.height)] for x in range(self.width)])
        self.depth = np.array([[float("inf") for y in range(self.height)] for x in range(self.width)])

    def plotRaw(self, coordinate: point2D, text: str) -> None:
        self.frame[round(coordinate.getX())][round(coordinate.getY())] = text

    def plotPoints(self, a: np.array/list) -> None:
        for item in a:
            coordinate, coordinateDepth, shading = item
            if 0 <= round(coordinate.getX()) < self.width and 0 <= round(coordinate.getY()) < self.height and coordinateDepth <= self.depth[round(coordinate.getX())][round(coordinate.getY())]:
                self.frame[round(coordinate.getX())][round(coordinate.getY())] = shading
                self.depth[round(coordinate.getX())][round(coordinate.getY())] = coordinateDepth

    def edgeFunction(self, a: np.array, b: np.array, p: np.array) -> float:
        return ((b[0] - a[0]) * (p[1] - a[1])) - ((b[1] - a[1]) * (p[0] - a[0]))

    def fillTri(self, vertex0: np.array, vertex1: np.array, vertex2: np.array, depth0: float, depth1: float, depth2: float, shading: str) -> None:
        area = self.edgeFunction(vertex0, vertex1, vertex2)
        if area == 0:
            return

        minX = max(0, min(vertex0[0], vertex1[0], vertex2[0]))
        maxX = min(self.width - 1, max(vertex0[0], vertex1[0], vertex2[0]))
        minY = max(0, min(vertex0[1], vertex1[1], vertex2[1]))
        maxY = min(self.height - 1, max(vertex0[1], vertex1[1], vertex2[1]))

        filledPixels = []
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                pixel = np.array([x, y])
                weight0 = self.edgeFunction(vertex1, vertex2, pixel) / area
                weight1 = self.edgeFunction(vertex2, vertex0, pixel) / area
                weight2 = self.edgeFunction(vertex0, vertex1, pixel) / area

                if weight0 >= 0 and weight1 >= 0 and weight2 >= 0:
                    pixelDepth = 1 / ((weight0 / depth0) + (weight1 / depth1) + (weight2 / depth2)) # weighted average depth
                    filledPixels.append((point2D(x, y), pixelDepth, shading))

        self.plotPoints(filledPixels)

    def show(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in reversed(list(zip(*self.frame))): # not ashamed to admit i googled this
            print("".join(row))