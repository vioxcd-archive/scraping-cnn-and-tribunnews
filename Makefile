all: whoopsie

tribun:
	python3 tribun-bs4/scrapers.py

cnn:
	python3 cnn-selenium/link-extractor.py

whoopsie:
	echo "whoopsie"