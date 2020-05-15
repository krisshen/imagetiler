import unittest
from imagetiler import tiler

class ImageTilerUnitTests(unittest.TestCase):

    def test_validate_file_path(self):
        imagePath = './images/123.png'
        self.assertRaises(FileNotFoundError, tiler.parse, imagePath)

    def test_get_size(self):
        imagePath = './images/cat1.png'
        tiler.parse(imagePath)
        self.assertEquals(tiler.size_x, 987)
        self.assertEquals(tiler.size_y, 660)

    def test_get_level(self):
        imagePath = './images/cat1.png'
        tiler.parse(imagePath)
        self.assertEquals(tiler.totalLevel, 11)

        self.assertEquals(tiler.getTotalLevel(512, 2), 10)
        self.assertEquals(tiler.getTotalLevel(800, 2), 11)