import mathLibrary as ml
import random

def flat(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)

    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gourad(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = ml.array([nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)

    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
    
def unlit(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    return r, g, b


def toon(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal =[nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]


    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)
    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)   
    #dirLight = np.array(render.dirLight)
    #intensity = np.dot(triangleNormal, -dirLight)

    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.8:
        intensity = 0.7
    elif intensity <= 1:
        intensity = 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def glow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)
    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)   
    #dirLight = np.array(render.dirLight)
    #intensity = np.dot(triangleNormal, -dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (ml.getMatrixValue(render.camMatrix, 0, 2),
                  ml.getMatrixValue(render.camMatrix, 1, 2),
                  ml.getMatrixValue(render.camMatrix, 2, 2))

    glowAmount = 1 - ml.dot_twoVectorsOfSameSize(triangleNormal, camForward)  
    #glowAmount = 1 - np.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    yellow = (1,0,0)

    b += yellow[2] * glowAmount
    g += yellow[1] * glowAmount
    r += yellow[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def textureBlend(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)
    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)   
    #dirLight = np.array(render.dirLight)
    #intensity = np.dot(triangleNormal, -dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if render.active_texture2:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor2 = render.active_texture2.getColor(tU, tV)

        b += (1 - intensity) * texColor2[2]
        g += (1 - intensity) * texColor2[1]
        r += (1 - intensity) * texColor2[0]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if b < 0: b = 0
    if g < 0: g = 0
    if r < 0: r = 0

    return r, g, b



def rgbGlow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)

    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)

    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity < 0.2:
        r = 1
    elif intensity < 0.5:
        g = 1
    elif intensity < 0.8:
        b = 1

    

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def static(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= random.random()
        g *= random.random()
        r *= random.random()

    triangleNormal = ml.array([nA[0] * u + nB[0] * v + nC[0] * w,
                                nA[1] * u + nB[1] * v + nC[1] * w,
                                nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)

    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)

    return r,g,b


def white(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[1]
        g *= texColor[1]
        r *= texColor[1]

    triangleNormal = ml.array([nA[0] * u + nB[0] * v + nC[0] * w,
                                nA[1] * u + nB[1] * v + nC[1] * w,
                                nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)

    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)

    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 1,1,1


def heatmap(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = ml.array([nA[0] * u + nB[0] * v + nC[0] * w,
                                nA[1] * u + nB[1] * v + nC[1] * w,
                                nA[2] * u + nB[2] * v + nC[2] * w])

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)

    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)

    
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity < 0.5:
        b = 1
    elif intensity < 0.7 and intensity >= 0.5:
        g = 1
    elif intensity <= 1 and intensity >= 0.7:
        r = 1


    if intensity > -0.8:
        return r, g, b
    else:
        return 1,0,0


def pinkjelly(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    blackwhite = [1.0,0,1.0]
    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w
        
        texColor = render.active_texture.getColor(tU, tV)

        b *= blackwhite[2]
        g *= texColor[1]
        r *= blackwhite[0]

    return r, g, b


def purpleGlow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = ml.array(render.dirLight)
    negDirLight = ml.negativeArray(dirLight)
    intensity = ml.dot_twoVectorsOfSameSize(triangleNormal, negDirLight)   
    #dirLight = np.array(render.dirLight)
    #intensity = np.dot(triangleNormal, -dirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (ml.getMatrixValue(render.camMatrix, 0, 2),
                  ml.getMatrixValue(render.camMatrix, 1, 2),
                  ml.getMatrixValue(render.camMatrix, 2, 2))

    glowAmount = 1 - ml.dot_twoVectorsOfSameSize(triangleNormal, camForward)  
    #glowAmount = 1 - np.dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    purple = (0.8,0.5,0.9)

    b += purple[2] * glowAmount
    g += purple[1] * glowAmount
    r += purple[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0