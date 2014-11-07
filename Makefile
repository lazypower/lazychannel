clean:
	@find -type f -name *.pyc -delete

clean-all: clean
	@rm -rf lazychannel.egg-info build dist
