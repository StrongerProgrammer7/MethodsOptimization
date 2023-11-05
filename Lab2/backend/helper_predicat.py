
def isNotZeroPoints(arr, frame):
    return abs(round(arr[frame][0])) != 0 and abs(round(arr[frame][1])) != 0 and abs(round(arr[frame][2])) != 0


def isNotEmptyFields(arrFields):
    for i in arrFields:
        if i.get() == "" and int(i.get()) == 0:
            print(int(i.get()))
            return False
    return True


def isNotOutGraphic(START,END,min_x, max_x, min_y, max_y):
    return START <= min_x <= END and min_x < max_x and START <= max_x <= END and \
        START <= min_y <= END and min_y < max_y and START <= max_y <= END
