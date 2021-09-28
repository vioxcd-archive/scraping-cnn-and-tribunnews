all: whoopsie

tribun:
	python3 tribun-bs4/scrapers.py

cnn:
	python3 cnn-selenium/scrapers.py

whoopsie:
	echo "whoopsie"