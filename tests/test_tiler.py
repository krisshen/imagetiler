import unittest
import math
import os
from os import path
import shutil
from imagetiler import tiler
from PIL import Image, UnidentifiedImageError


class ImageTilerUnitTests(unittest.TestCase):

    def cleanUp(self):
        if path.exists('./output'):
            shutil.rmtree('./output')

    def test_file_path_not_exist(self):
        imagePath = './images/non_exist_file.png'
        self.assertRaises(FileNotFoundError, tiler.validateFilePath, imagePath)

    def test_not_supported_file_format(self):
        imagePath = './images/not-an-image.txt'
        self.assertRaises(UnidentifiedImageError, tiler.parse, imagePath)

    def test_get_output_path(self):
        imagePath = './a.b/images/cat1.png'
        self.assertEqual(tiler.getOutputPath(imagePath), os.path.dirname(os.path.realpath(imagePath)) + '/cat1')
        
    def test_get_size(self):
        img = Image.open('./images/cat1.png')
        x, y = tiler.getImageSize(img)

        self.assertEqual(x, 987)
        self.assertEqual(y, 660)

    def test_get_total_level(self):
        self.assertEqual(tiler.getTotalLevel(512, 256), 10)
        self.assertEqual(tiler.getTotalLevel(513, 256), 11)
        self.assertEqual(tiler.getTotalLevel(256, 800), 11)
        self.assertEqual(tiler.getTotalLevel(7000, 5000),
                         1 + round(math.log2(7000)))

    def test_size_per_layer(self):
        levels = tiler.calcAllLevelsSize(987, 660, 11)

        self.assertEqual(levels[10], (987, 660))
        self.assertEqual(levels[9], (494, 330))
        self.assertEqual(levels[8], (247, 165))
        self.assertEqual(levels[7], (124, 83))
        self.assertEqual(levels[6], (62, 42))
        self.assertEqual(levels[5], (31, 21))
        self.assertEqual(levels[4], (16, 11))
        self.assertEqual(levels[3], (8, 6))
        self.assertEqual(levels[2], (4, 3))
        self.assertEqual(levels[1], (2, 2))
        self.assertEqual(levels[0], (1, 1))

    # @unittest.skip("skip it")
    def test_resize_image1(self):

        self.cleanUp()

        # test cat1.png, size: 987 x 660
        imagePath = './images/cat1.png'
        img = Image.open(imagePath)
        img = img.convert("RGB")
        x, y = tiler.getImageSize(img)
        level = tiler.getTotalLevel(x, y)
        levels = tiler.calcAllLevelsSize(x, y, level)
        outputPath = './output'

        tiler.resizeAndCropImage(img, levels, outputPath)

        # check total tiles in each level
        self.assertEqual(len(os.listdir('./output/10')), 12)
        self.assertEqual(len(os.listdir('./output/9')), 4)
        self.assertEqual(len(os.listdir('./output/8')), 1)
        self.assertEqual(len(os.listdir('./output/0')), 1)

        # check file size for edge ones
        # top right
        img = Image.open('./output/10/768_0.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 219)
        self.assertEqual(actual_y, 256)
        # bottom right
        img = Image.open('./output/10/768_512.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 219)
        self.assertEqual(actual_y, 148)
        # bottom left
        img = Image.open('./output/10/0_512.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 256)
        self.assertEqual(actual_y, 148)

    # @unittest.skip("skip it")
    def test_resize_image2(self):

        self.cleanUp()

        # test cat2.jpg: size: 1920 x 1440
        imagePath = './images/cat2.jpg'
        img = Image.open(imagePath)
        x, y = tiler.getImageSize(img)
        level = tiler.getTotalLevel(x, y)
        levels = tiler.calcAllLevelsSize(x, y, level)
        outputPath = './output'

        tiler.resizeAndCropImage(img, levels, outputPath)

        # check total tiles in each level
        self.assertEqual(len(os.listdir('./output/11')), 48)
        self.assertEqual(len(os.listdir('./output/10')), 12)
        self.assertEqual(len(os.listdir('./output/9')), 4)
        self.assertEqual(len(os.listdir('./output/8')), 1)
        self.assertEqual(len(os.listdir('./output/0')), 1)

        # check file size for edge ones
        # top right
        img = Image.open('./output/11/1792_0.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 128)
        self.assertEqual(actual_y, 256)
        # bottom right in level 11
        img = Image.open('./output/11/1792_1280.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 128)
        self.assertEqual(actual_y, 160)
        # bottom right in level 10
        img = Image.open('./output/10/768_512.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 192)
        self.assertEqual(actual_y, 208)

    # @unittest.skip("skip it")
    def test_resize_image3(self):

        self.cleanUp()

        # test cat2.jpg: size: 1960 x 4032
        imagePath = './images/cat3.jpg'
        img = Image.open(imagePath)
        x, y = tiler.getImageSize(img)
        level = tiler.getTotalLevel(x, y)
        levels = tiler.calcAllLevelsSize(x, y, level)
        outputPath = './output'

        tiler.resizeAndCropImage(img, levels, outputPath)

        # check total tiles in each level
        self.assertEqual(len(os.listdir('./output/12')), 128)
        self.assertEqual(len(os.listdir('./output/11')), 32)
        self.assertEqual(len(os.listdir('./output/10')), 8)
        self.assertEqual(len(os.listdir('./output/9')), 2)
        self.assertEqual(len(os.listdir('./output/8')), 1)

    def test_resize_image4(self):

        self.cleanUp()

        # test cat2.jpg: size: 5100 x 2869
        imagePath = './images/cat4.jpg'
        img = Image.open(imagePath)
        x, y = tiler.getImageSize(img)
        level = tiler.getTotalLevel(x, y)
        levels = tiler.calcAllLevelsSize(x, y, level)
        outputPath = './output'

        tiler.resizeAndCropImage(img, levels, outputPath)

        # check total tiles in each level
        self.assertEqual(len(os.listdir('./output/13')), 240)
        self.assertEqual(len(os.listdir('./output/12')), 60)
        self.assertEqual(len(os.listdir('./output/11')), 15)
        self.assertEqual(len(os.listdir('./output/10')), 6)
        self.assertEqual(len(os.listdir('./output/9')), 2)
        self.assertEqual(len(os.listdir('./output/8')), 1)
        self.assertEqual(len(os.listdir('./output/0')), 1)

        # image size in level 0 should be (1, 1)
        img = Image.open('./output/0/0_0.jpg')
        actual_x, actual_y = tiler.getImageSize(img)
        self.assertEqual(actual_x, 1)
        self.assertEqual(actual_y, 1)
