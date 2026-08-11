.PHONY: sync html serve clean

sync:
	python3 tools/sync_source_docs.py

html:
	mkdocs build --strict

serve:
	mkdocs serve

clean:
	rm -rf site
