
# Introduction

This code base is a simple **Image Tiler** utility (Python module) written in Python 3. It reads an input image, calculate its levels (based on 1/2 resolution, 1/4 resolution and so on until 1x1) and size per each level, then generates 256x256 sized tiles for the entire image per level, which means all tiles will make up to a full image.

**Input:** an image file path, e.g. "./images/cat1.png"

**Output:** a directory with the same image name will be created in the same path of input image, and this directory consists of tiles in each level, naming convention: "./images/cat1/{Level}/{x}_{y}.jpg" - x, y are top left coordinates of the tile.

**Note:** This utility assumes the input file path is also writable.

**User interface:** MakeFile and Python CLI. 

It's built with TDD approach for practise :) 


# Prerequisites

-  [Python 3](https://www.python.org/downloads/)

- (Tested in) Mac OS

# Install

	make setup
	
# Usage

## How to run

Two ways to run:

	# use MakeFile command, replace {IMAGE_PATH} with your actual image path
	make run IMAGEPATH="{IMAGE_PATH}"

	# or use Python command, replace {IMAGE_PATH} with your actual image path
	python3 imagetiler/tiler.py "{IMAGE_PATH}"


## Output

A directory with the same image name will be created in the same path of input image

# Tests

## Python Unittest Execution
   
    # use MakeFile command
	make test

## Scenarios Covered

-  Error handling, input file not exist
-  Error handling, input file format not supported
-  Error handling, input file content not correct
-  Tricky case, input file path contains extra dots, e.g. './a.b/images/cat1.png'
-  Tricky case, input file path contains space (tested manually)
-  validate input file size
-  validate total levels calculation
-  validate each level's overall size
-  validate resize and crop functions for different image size (tested manually, very large one 24mb image not uploaded into this repo)


# Dependencies

-  [Pillow](https://pillow.readthedocs.io/en/stable/)

# Assumptions/Limitations

-  I have multiple versions of Python installed, so I'm using 'python3' in this utility for running all Python related commands.
-  Input image path should be writable.
-  Not tested with all image formats, for now it supports PNG and JPEG.
-  Tested with input path (with space) manually.
-  Got "ResourceWarning: unclosed file " warning when executing unit tests, not a blocker though, may need more investigation.
-  This Python module is built in pure module functions, using Class may better hide the details other than exposing them. 
It's also easier to understand code logic when manipulating objects other than functions and variables directly.
-  Edge tiles are cut off as they are not fully 256 x 256 size.
-  More unit tests could be added to validate tile's binary data.
-  A proper test reporting library might be integrated for better reporting.
-  May utilize docker to make execution more isolated and independent.

# Others

## PNG file size is sometimes too big, need to convert to JPG first, code sample:

	img = Image.open('xxx.png')
    img = img.convert("RGB")
	img.save('xxx.jpg')


 
