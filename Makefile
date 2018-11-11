.PHONY: build upgrade db clean

setup:
	pip3 install --upgrade setuptools wheel twine

build:
	pandoc README.md -o README.rst
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

db:
	python3 -m emojis.db.generator --dir ./emojis/db/ --dbname db.py

clean:
	rm -rf build
	rm -rf dist
	rm -rf emojis/__pycache__
	rm -rf emojis/db/__pycache__
