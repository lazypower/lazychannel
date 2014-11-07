.PHONY: test clean clean_all lint

all: setup develop lint coverage

clean:
	find . -name \*.pyc -delete
	find . -name '*.bak' -delete
	rm -f .coverage

clean-all: clean
	rm -rf venv

venv/bin/python:
	virtualenv venv
	venv/bin/pip install 'distribute>=0.6.45'

test: develop
	@venv/bin/nosetests tests

coverage: develop clean
	@venv/bin/nosetests tests --with-coverage --cover-package=lazychannel

lint: develop
	@find $(sources) -type f \( -iname '*.py' ! -iwholename './venv/*' ! -iwholename './tests/*' \) -print0 | xargs -r0 venv/bin/flake8

develop: setup venv/lib/python*/site-packages/lazychannel.egg-link
venv/lib/python*/site-packages/lazychannel.egg-link:
	venv/bin/python setup.py develop

setup: venv/bin/python
	venv/bin/pip install -q -r requirements.txt
