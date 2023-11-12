
def isNotZeroPoints(arr, frame):
    return abs(round(arr[frame][0])) != 0 and abs(round(arr[frame][1])) != 0 and abs(round(arr[frame][2])) != 0


def isNotEmptyFields(arrFields):
    for i in arrFields:
        if i.get() == "" and int(i.get()) == 0:
            print(int(i.get()))
            return False
    return True

def isNotOutGraphicDict(START,END,min_x, max_x, min_y, max_y):
    return START[1] >= min_x <= START[2] and min_x < max_x and START[1] <= max_x and max_x >= START[2] and \
        END[1] >= min_y <= END[2] and min_y < max_y and END[1] <= max_y >= END[2]

def isNotOutGraphic(START,END,min_x, max_x, min_y, max_y):
    return START <= min_x <= END and min_x < max_x and START <= max_x <= END and \
        START <= min_y <= END and min_y < max_y and START <= max_y <= END
