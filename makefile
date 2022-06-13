all:
	python3 display.py
clean:
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm *.spec
