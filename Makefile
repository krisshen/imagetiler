setup:
	pip3 install .

test:
	python3 setup.py test

run:
	python3 imagetiler/tiler.py "${IMAGEPATH}"