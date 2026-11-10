import siffrinderprimitives as prim, numpy as np, time

cube = prim.model(np.array([prim.tri(prim.point3D(-0.5,-0.5,-0.5), prim.point3D(0.5,-0.5,-0.5), prim.point3D(0.5,0.5,-0.5)),
prim.tri(prim.point3D(-0.5,-0.5,-0.5), prim.point3D(-0.5,0.5,-0.5), prim.point3D(0.5,0.5,-0.5)),
prim.tri(prim.point3D(-0.5,-0.5,-0.5), prim.point3D(-0.5,-0.5,0.5), prim.point3D(-0.5,0.5,0.5)),
prim.tri(prim.point3D(-0.5,-0.5,-0.5), prim.point3D(-0.5,0.5,-0.5), prim.point3D(-0.5,0.5,0.5)),
prim.tri(prim.point3D(-0.5,-0.5,0.5), prim.point3D(0.5,-0.5,0.5), prim.point3D(0.5,0.5,0.5)),
prim.tri(prim.point3D(-0.5,-0.5,0.5), prim.point3D(-0.5,0.5,0.5), prim.point3D(0.5,0.5,0.5)),
prim.tri(prim.point3D(0.5,-0.5,-0.5), prim.point3D(0.5,-0.5,0.5), prim.point3D(0.5,0.5,0.5)),
prim.tri(prim.point3D(0.5,-0.5,-0.5), prim.point3D(0.5,0.5,-0.5), prim.point3D(0.5,0.5,0.5)),
prim.tri(prim.point3D(-0.5,-0.5,-0.5), prim.point3D(-0.5,-0.5,0.5), prim.point3D(0.5,-0.5,-0.5)),
prim.tri(prim.point3D(0.5,-0.5,0.5), prim.point3D(-0.5,-0.5,0.5), prim.point3D(0.5,-0.5,-0.5)),
prim.tri(prim.point3D(-0.5,0.5,-0.5), prim.point3D(-0.5,0.5,0.5), prim.point3D(0.5,0.5,-0.5)),
prim.tri(prim.point3D(0.5,0.5,0.5), prim.point3D(-0.5,0.5,0.5), prim.point3D(0.5,0.5,-0.5))])) # this took me 20 minutes and a whiteboard to work out btw

cam = prim.camera(np.array([0, 0, -2]), np.array([0, 0, 0]), np.array([20, 10, 18]))
display = prim.screen(40, 30)

while True:
    display.newFrame()
    points = np.empty((0, 2))

    for triEdge in cube.getEdges():
        for line in triEdge:
            endpoints = line.getEndpoints()
            screenLine = prim.line2D(prim.point2D(*cam.projection2D(endpoints.item(0).getCoordinates())), prim.point2D(*cam.projection2D(endpoints.item(1).getCoordinates()))) # i hate this line
            points = np.append(points, screenLine.getCoordinates(), axis=0)

    display.plotPoints(points)
    display.show()
    cube.rotateOrigin(np.array([2, 3, 1]))
    time.sleep(1/60)
