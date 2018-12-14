SPHINXOPTS    = -a
SPHINXBUILD   = sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build
PYTHON        = python3
PANDOC        = pandoc
PIP           = pip3

.PHONY: setup pandoc build upload db test docs clean

setup:
	$(PIP) install --upgrade requests setuptools wheel twine sphinx

pandoc:
	$(PANDOC) README.md -o README.rst

build: clean pandoc
	$(PYTHON) setup.py sdist bdist_wheel

upload:
	twine upload dist/*

db:
	$(PYTHON) ./emojis/db/generator.py --dir ./emojis/db/ --dbname db.py

test:
	$(PYTHON) -m tests.test -v

docs: pandoc
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	rm -rf README.rst
	rm -rf build
	rm -rf dist
	rm -rf emojis.egg-info
	rm -rf emojis/__pycache__
	rm -rf emojis/db/__pycache__
