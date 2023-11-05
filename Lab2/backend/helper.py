

def getMatrixFromList(resultFunction):
    temp = []
    tx,ty,tz = None,None,None
    for x, y, f in resultFunction:
        if tx != None and ty != None and tz != None and tx == x and ty == y and tz == f:
            continue
        temp.append([x, y, f])
        tx,ty,tz = x,y,f
    return temp


def getMatrixFromMatrixList(points):
    new_matrix = []
    for i in range(len(points)):
        for x,y,z in points[i]:
            new_matrix.append([x,y,z])
    return new_matrix

def deleteDuplicateValue(matrix):
    newMatrix = []
    tx,ty = None , None
    lastPoint = matrix[len(matrix)-1]
    for arr in matrix:
        if tx != None and ty != None and tx == round(arr[0],5) and ty == round(arr[1],5) and arr[0] != lastPoint[0] and arr[1] != lastPoint[1]:
            continue
        newMatrix.append(arr)
        tx = round(arr[0],5)
        ty = round(arr[1],5)
    return newMatrix