import primitives

cube = primitives.model(np.array([primitives.tri(primtives.point3D(0,0,0), primtives.point3D(1,0,0), primtives.point3D(1,1,0)),
primitives.tri(primtives.point3D(0,0,0), primtives.point3D(0,1,0), primtives.point3D(1,1,0)),
primitives.tri(primtives.point3D(0,0,0), primtives.point3D(0,0,1), primtives.point3D(0,1,1)),
primitives.tri(primtives.point3D(0,0,0), primtives.point3D(0,1,0), primtives.point3D(0,1,1)),
primitives.tri(primtives.point3D(0,0,1), primtives.point3D(1,0,1), primtives.point3D(1,1,1)),
primitives.tri(primtives.point3D(0,0,1), primtives.point3D(0,1,1), primtives.point3D(1,1,1)),
primitives.tri(primtives.point3D(1,0,0), primtives.point3D(1,0,1), primtives.point3D(1,1,1)),
primitives.tri(primtives.point3D(1,0,0), primtives.point3D(1,1,0), primtives.point3D(1,1,1)),
primitives.tri(primtives.point3D(0,0,0), primtives.point3D(0,0,1), primtives.point3D(1,0,0)),
primitives.tri(primtives.point3D(1,0,1), primtives.point3D(0,0,1), primtives.point3D(1,0,0)),
primitives.tri(primtives.point3D(0,1,0), primtives.point3D(0,1,1), primtives.point3D(1,1,0)),
primitives.tri(primtives.point3D(1,1,1), primtives.point3D(0,1,1), primtives.point3D(1,1,0))]))