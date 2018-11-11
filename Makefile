.PHONY: build upgrade db test clean

setup:
	pip3 install --upgrade setuptools wheel twine

build: clean
	pandoc README.md -o README.rst
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

db:
	python3 -m emojis.db.generator --dir ./emojis/db/ --dbname db.py

test:
	python3 -m tests.test -v

clean:
	rm -rf README.rst
	rm -rf build
	rm -rf dist
	rm -rf emojis.egg-info
	rm -rf emojis/__pycache__
	rm -rf emojis/db/__pycache__
