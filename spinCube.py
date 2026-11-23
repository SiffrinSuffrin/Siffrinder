import siffrinderPrimitives as prim, numpy as np, time, random

colours = [(0, 154, 68), (186, 12, 47), (0, 61, 165), (254, 80, 0), (255, 215, 0), (255, 255, 255)]

faceShading0, faceTexture0 = colours.pop(), "0"
faceShading1, faceTexture1 = colours.pop(), "1"
faceShading2, faceTexture2 = colours.pop(), "2"
faceShading3, faceTexture3 = colours.pop(), "3"
faceShading4, faceTexture4 = colours.pop(), "4"
faceShading5, faceTexture5 = colours.pop(), "5"

cube = prim.model(np.array([
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(1,-1,-1), prim.point3D(1,1,-1), faceShading0, f"{faceTexture0*2}"),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,1,-1), prim.point3D(1,1,-1), faceShading0, f"{faceTexture0*2}"),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,-1,1), prim.point3D(-1,1,1), faceShading1, f"{faceTexture1*2}"),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,1,-1), prim.point3D(-1,1,1), faceShading1, f"{faceTexture1*2}"),
prim.tri(prim.point3D(-1,-1,1), prim.point3D(1,-1,1), prim.point3D(1,1,1), faceShading2, f"{faceTexture2*2}"),
prim.tri(prim.point3D(-1,-1,1), prim.point3D(-1,1,1), prim.point3D(1,1,1), faceShading2, f"{faceTexture2*2}"),
prim.tri(prim.point3D(1,-1,-1), prim.point3D(1,-1,1), prim.point3D(1,1,1), faceShading3, f"{faceTexture3*2}"),
prim.tri(prim.point3D(1,-1,-1), prim.point3D(1,1,-1), prim.point3D(1,1,1), faceShading3, f"{faceTexture3*2}"),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,-1,1), prim.point3D(1,-1,-1), faceShading4, f"{faceTexture4*2}"),
prim.tri(prim.point3D(1,-1,1), prim.point3D(-1,-1,1), prim.point3D(1,-1,-1), faceShading4, f"{faceTexture4*2}"),
prim.tri(prim.point3D(-1,1,-1), prim.point3D(-1,1,1), prim.point3D(1,1,-1), faceShading5, f"{faceTexture5*2}"),
prim.tri(prim.point3D(1,1,1), prim.point3D(-1,1,1), prim.point3D(1,1,-1), faceShading5, f"{faceTexture5*2}")
])) # this took me 20 minutes and a whiteboard to work out btw

cam = prim.camera(np.array([0, 0, -2.5]), np.array([0, 0, 0]), np.array([20, 15, 18]))
display = prim.screen(40, 32)

frameTime = 1/60

while True:
    startTime = time.perf_counter()
    display.newFrame()
    cube.rotateOrigin(np.array([(2*60)*frameTime, (3*60)*frameTime, (1*60)*frameTime]))
    points = []

    for tri in cube.getTri():
        vertex0, depth0 = cam.projection2D(tri.vertex0.getCoordinates())
        vertex1, depth1 = cam.projection2D(tri.vertex1.getCoordinates())
        vertex2, depth2 = cam.projection2D(tri.vertex2.getCoordinates())
        display.plotTri(vertex0, vertex1, vertex2, depth0, depth1, depth2, tri.getShading(), tri.getTexture())

    display.plotPoints(points)
    endTime = time.perf_counter()
    display.plotRaw(prim.point2D(0,display.height-1), round((endTime-startTime)*(10**3)))
    display.plotRaw(prim.point2D(1,display.height-1), "ms")
    display.show()
    sleepTime = (1 / 60) - (endTime - startTime)
    frameTime = (1 / 60) + (endTime - startTime)
    if sleepTime > 0:
        time.sleep(sleepTime)