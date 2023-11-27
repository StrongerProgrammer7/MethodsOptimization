from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    CYAN = "cyan"
    YELLOW = "yellow"
    PINK = "pink"
    BLACK = "black"
    WHITE = "white"
    GRAY = "gray"
class ColorFigure(Enum):
    PLASMA = "plasma"
    VIRIDIS = "viridis"
    INFERNO = "inferno"
    MAGMA = "magma"
    CIVIDIS = "cividis"
    BINARY = "binary"
    SPRING = "spring"
    SUMMER = "summer"
    WINTER = "winter"
    AUTUMN = "autumn"
    BONE = "bone"

colors_3DGraphic = {
    "plasma": ColorFigure.PLASMA.value,
    "viridis":ColorFigure.VIRIDIS.value,
    "inferno":ColorFigure.INFERNO.value,
    "magma":ColorFigure.MAGMA.value,
    "cividis":ColorFigure.CIVIDIS.value,
    "binary":ColorFigure.BINARY.value,
    "spring":ColorFigure.SPRING.value,
    "summer":ColorFigure.SUMMER.value,
    "winter":ColorFigure.WINTER.value,
    "autumn":ColorFigure.AUTUMN.value,
    "bone":ColorFigure.BONE.value
}

colors_points = {
    "red": Color.RED.value,
    "green":Color.GREEN.value,
    "blue":Color.BLUE.value,
    "cyan":Color.CYAN.value,
    "yellow":Color.YELLOW.value,
    "pink":Color.PINK.value,
    "black":Color.BLACK.value,
    "white":Color.WHITE.value,
    "gray":Color.GRAY.value,
}