import primitives, numpy as np, time

cube = primitives.model(np.array([primitives.tri(primitives.point3D(0,0,0), primitives.point3D(1,0,0), primitives.point3D(1,1,0)),
primitives.tri(primitives.point3D(0,0,0), primitives.point3D(0,1,0), primitives.point3D(1,1,0)),
primitives.tri(primitives.point3D(0,0,0), primitives.point3D(0,0,1), primitives.point3D(0,1,1)),
primitives.tri(primitives.point3D(0,0,0), primitives.point3D(0,1,0), primitives.point3D(0,1,1)),
primitives.tri(primitives.point3D(0,0,1), primitives.point3D(1,0,1), primitives.point3D(1,1,1)),
primitives.tri(primitives.point3D(0,0,1), primitives.point3D(0,1,1), primitives.point3D(1,1,1)),
primitives.tri(primitives.point3D(1,0,0), primitives.point3D(1,0,1), primitives.point3D(1,1,1)),
primitives.tri(primitives.point3D(1,0,0), primitives.point3D(1,1,0), primitives.point3D(1,1,1)),
primitives.tri(primitives.point3D(0,0,0), primitives.point3D(0,0,1), primitives.point3D(1,0,0)),
primitives.tri(primitives.point3D(1,0,1), primitives.point3D(0,0,1), primitives.point3D(1,0,0)),
primitives.tri(primitives.point3D(0,1,0), primitives.point3D(0,1,1), primitives.point3D(1,1,0)),
primitives.tri(primitives.point3D(1,1,1), primitives.point3D(0,1,1), primitives.point3D(1,1,0))])) # this took me 20 minutes and a whiteboard to work out btw

cam = primitives.camera(np.array([0, 0, -2]), np.array([0, 0, 0]), np.array([20, 10, 18]))
display = primitives.screen(40, 30)

while True:
    points = np.empty((0, 2))

    for triEdge in cube.getEdges():
        for line in triEdge:
            endpoints = line.getEndpoints()
            screenLine = primitives.line2D(primitives.point2D(*cam.projection2D(endpoints.item(0).getCoordinates())), primitives.point2D(*cam.projection2D(endpoints.item(1).getCoordinates()))) # i hate this line
            points = np.append(points, screenLine.getCoordinates(), axis=0)

    display.drawOut(points)
    cube.rotateOrigin(np.array([2, 3, 1]))
    time.sleep(0.05)
