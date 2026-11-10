import siffrinderPrimitives as prim, numpy as np, time

cube = prim.model(np.array([prim.tri(prim.point3D(-1,-1,-1), prim.point3D(1,-1,-1), prim.point3D(1,1,-1)),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,1,-1), prim.point3D(1,1,-1)),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,-1,1), prim.point3D(-1,1,1)),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,1,-1), prim.point3D(-1,1,1)),
prim.tri(prim.point3D(-1,-1,1), prim.point3D(1,-1,1), prim.point3D(1,1,1)),
prim.tri(prim.point3D(-1,-1,1), prim.point3D(-1,1,1), prim.point3D(1,1,1)),
prim.tri(prim.point3D(1,-1,-1), prim.point3D(1,-1,1), prim.point3D(1,1,1)),
prim.tri(prim.point3D(1,-1,-1), prim.point3D(1,1,-1), prim.point3D(1,1,1)),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,-1,1), prim.point3D(1,-1,-1)),
prim.tri(prim.point3D(1,-1,1), prim.point3D(-1,-1,1), prim.point3D(1,-1,-1)),
prim.tri(prim.point3D(-1,1,-1), prim.point3D(-1,1,1), prim.point3D(1,1,-1)),
prim.tri(prim.point3D(1,1,1), prim.point3D(-1,1,1), prim.point3D(1,1,-1))])) # this took me 20 minutes and a whiteboard to work out btw

cam = prim.camera(np.array([0, 0, -2.5]), np.array([0, 0, 0]), np.array([20, 15, 18]))
display = prim.screen(40, 32)

while True:
    startTime = time.perf_counter()
    display.newFrame()
    cube.rotateOrigin(np.array([2, 3, 1]))
    points = np.array([])

    for triEdge in cube.getEdges():
        for line in triEdge:
            endpoints = line.getEndpoints()
            screenLine = prim.line2D(prim.point2D(*cam.projection2D(endpoints.item(0).getCoordinates())), prim.point2D(*cam.projection2D(endpoints.item(1).getCoordinates()))) # i hate this line
            points = np.append(points, screenLine.getCoordinates())

    display.plotPoints(points)
    endTime = time.perf_counter()
    display.plotRaw(prim.point2D(0,display.height-1), round((endTime-startTime)*(10**3)))
    display.plotRaw(prim.point2D(1,display.height-1), "ms")
    display.show()
    sleepTime = (1 / 60) - (endTime - startTime)
    if sleepTime > 0:
        time.sleep(sleepTime)
