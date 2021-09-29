all: whoopsie

setup:
	python3 setup-dump.py

tribun:
	python3 tribun-bs4/scrapers.py

cnn-link:
	python3 cnn-selenium/link-extractor.py

cnn-page:
	python3 cnn-selenium/scrapers.py

whoopsie:
	echo "whoopsie"