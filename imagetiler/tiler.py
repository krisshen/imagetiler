import math
import sys
from os import path
from PIL import Image


def parse(imagePath):
    if not path.exists(imagePath):
        raise FileNotFoundError

    img = Image.open(imagePath)

    global size_x, size_y, totalLevel

    size_x, size_y = img.size

    totalLevel = getTotalLevel(size_x, size_y)


def getTotalLevel(x, y):
    return round(math.log2(max(x, y)) + 1)


def log(number):
    return math.log2(number)


def main():
    parse(sys.argv[1])


if __name__ == "__main__":
    # execute only if run as a script
    main()
