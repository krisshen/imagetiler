import math
import sys
import os
from os import path
from PIL import Image


def parse(imagePath):

    validateFilePath(imagePath)

    outputPath = getOutputPath(imagePath)
    # print("file path: " + outputPath)

    img = Image.open(imagePath)
    if img.format != "JPEG":
        img = img.convert("RGB")  # convert to JPG
        print("converted to JPG format")

    global size_x, size_y, totalLevel, levels

    size_x, size_y = getImageSize(img)

    # calculate total levels
    totalLevel = getTotalLevel(size_x, size_y)
    print("total level is: " + str(totalLevel))
    # calculate all level's size
    levels = calcAllLevelsSize(size_y, size_y, totalLevel)

    # get bounding box coordinates
    left, upper, right, lower = img.getbbox()

    # some real work on images
    resizeAndCropImage(img, levels, outputPath)


def getOutputPath(path):
    return os.path.splitext(os.path.realpath(path))[0]
    # 


# resize and crop image for each level
def resizeAndCropImage(img, levels, outputPath):

    for level, size in levels.items():
        # shrink
        _img = img.resize(size)

        # print("level: ", str(level), ", size: ", _img.size)

        # create dirs
        dirPath = outputPath + '/' + str(level) + '/'
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        # get current x, y
        x = size[0]
        y = size[1]

        left = 0
        for m in range(math.ceil(x / 256)):
            upper = 0
            for n in range(math.ceil(y / 256)):
                right = left + 256
                lower = upper + 256
                box = (left, upper, right if right < x else x, lower if lower < y else y)
                subImg = _img.crop(box)
                subImgPath = dirPath + str(left) + '_' + str(upper) + '.jpg'
                subImg.save(subImgPath)
                upper += 256
            left += 256


def validateFilePath(imagePath):
    if not path.exists(imagePath):
        raise FileNotFoundError


def getTotalLevel(x, y):
    # return round(math.log2(max(x, y)) + 1)
    return math.ceil(math.log2(max(x, y)) + 1)


def calcAllLevelsSize(x, y, l):
    res = {}
    _x = x
    _y = y
    for i in range(l-1, -1, -1):
        res[i] = (_x, _y)
        _x = math.ceil(_x / 2)
        _y = math.ceil(_y / 2)
    # print(res)
    return res


def getImageSize(img):
    return img.size


def log(number):
    return math.log2(number)


def main():
    parse(sys.argv[1])


if __name__ == "__main__":
    # execute only if run as a script
    main()
