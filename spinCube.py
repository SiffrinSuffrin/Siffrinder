import siffrinderPrimitives as prim, numpy as np, time, random

textures = [f"{chr(i)}{chr(i)}" for i in range(9600, 9632)]

faceShading0, faceTexture0 = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.choice(textures)
faceShading1, faceTexture1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.choice(textures)
faceShading2, faceTexture2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.choice(textures)
faceShading3, faceTexture3 = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.choice(textures)
faceShading4, faceTexture4 = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.choice(textures)
faceShading5, faceTexture5 = (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.choice(textures)

cube = prim.model(np.array([
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(1,-1,-1), prim.point3D(1,1,-1), faceShading0, faceTexture0),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,1,-1), prim.point3D(1,1,-1), faceShading0, faceTexture0),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,-1,1), prim.point3D(-1,1,1), faceShading1, faceTexture1),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,1,-1), prim.point3D(-1,1,1), faceShading1, faceTexture1),
prim.tri(prim.point3D(-1,-1,1), prim.point3D(1,-1,1), prim.point3D(1,1,1), faceShading2, faceTexture2),
prim.tri(prim.point3D(-1,-1,1), prim.point3D(-1,1,1), prim.point3D(1,1,1), faceShading2, faceTexture2),
prim.tri(prim.point3D(1,-1,-1), prim.point3D(1,-1,1), prim.point3D(1,1,1), faceShading3, faceTexture3),
prim.tri(prim.point3D(1,-1,-1), prim.point3D(1,1,-1), prim.point3D(1,1,1), faceShading3, faceTexture3),
prim.tri(prim.point3D(-1,-1,-1), prim.point3D(-1,-1,1), prim.point3D(1,-1,-1), faceShading4, faceTexture4),
prim.tri(prim.point3D(1,-1,1), prim.point3D(-1,-1,1), prim.point3D(1,-1,-1), faceShading4, faceTexture4),
prim.tri(prim.point3D(-1,1,-1), prim.point3D(-1,1,1), prim.point3D(1,1,-1), faceShading5, faceTexture5),
prim.tri(prim.point3D(1,1,1), prim.point3D(-1,1,1), prim.point3D(1,1,-1), faceShading5, faceTexture5)
])) # this took me 20 minutes and a whiteboard to work out btw

cam = prim.camera(np.array([0, 0, -2.5]), np.array([0, 0, 0]), np.array([20, 15, 18]))
display = prim.screen(40, 32)

while True:
    startTime = time.perf_counter()
    display.newFrame()
    cube.rotateOrigin(np.array([2, 3, 1]))
    points = []

    for tri in cube.getTri():
        vertex0, depth0 = cam.projection2D(tri.vertex0.getCoordinates())
        vertex1, depth1 = cam.projection2D(tri.vertex1.getCoordinates())
        vertex2, depth2 = cam.projection2D(tri.vertex2.getCoordinates())
        display.fillTri(vertex0, vertex1, vertex2, depth0, depth1, depth2, tri.getShading(), tri.getTexture())

    display.plotPoints(points)
    endTime = time.perf_counter()
    display.plotRaw(prim.point2D(0,display.height-1), round((endTime-startTime)*(10**3)))
    display.plotRaw(prim.point2D(1,display.height-1), "ms")
    display.show()
    sleepTime = (1 / 60) - (endTime - startTime)
    if sleepTime > 0:
        time.sleep(sleepTime)