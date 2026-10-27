PYTHON ?= python

.PHONY: install test verify lint paper package clean

install:
	$(PYTHON) -m pip install -e '.[dev]'

test:
	PYTHONPATH=src pytest -q

verify:
	PYTHONPATH=src $(PYTHON) -m rgphi.cli verify

lint:
	ruff check src tests

paper:
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex && pdflatex -interaction=nonstopmode -halt-on-error main.tex

package:
	$(PYTHON) tools/build_release.py

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache .ruff_cache
	rm -f paper/*.aux paper/*.log paper/*.out paper/*.fls paper/*.fdb_latexmk
