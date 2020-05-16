
# Introduction

This code base is a simple **Image Tiler** utility written in Python 3. 

User interface is Python CLI. 

It's built with TDD approach for practise :) 

# Prerequisites

-  [Python 3](https://www.python.org/downloads/)

- (Tested in) Mac OS

# Install

	make setup
	
# Usage

## How to run

Two ways to run:

	# use MakeFile command
	make run IMAGEPATH={IMAGE_PATH}

	# or use Python command
	python3 imagetiler/tiler.py {IMAGE_PATH}


## Output

Check output files in output foler after execution.

# Tests

	make test

# Dependencies

-  [Pillow](https://pillow.readthedocs.io/en/stable/)

# Problems Found

## PNG file size is too big, need to convert to JPG first, code sample:

	img = Image.open('xxx.png')
    img = img.convert("RGB")
	img.save('xxx.jpg')


 