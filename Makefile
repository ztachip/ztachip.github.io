SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = docs
BUILDDIR = _build

html:
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)"
