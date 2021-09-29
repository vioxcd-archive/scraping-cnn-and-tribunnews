# Scraping CNN & Tribun

Exracting page links in CNN using [Selenium](https://selenium-python.readthedocs.io/) & scraping CNN & Tribun pages using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

The [Scrapy](https://docs.scrapy.org/en/latest/index.html) code doesn't work. (fault on my part)

## How to Run

(easier using `make` command)

- Run `pip3 install -r requirements.txt`
- Download selenium browser drivers (based on which browser you're using: [chrome](http://chromedriver.storage.googleapis.com/index.html) or [gecko](https://github.com/mozilla/geckodriver/releases)) and include it in your `PATH`
- Setup dump folder structure using `make setup` or `python3 setup-dump.py`
- For Tribun, run `make tribun` or `python3 tribun-bs4/scrapers.py`
- For CNN:
  - First extract the links using `make cnn-link` or `python3 cnn-selenium/link-extractor.py`
  - Then, scrape page content using `make cnn-page` or `python3 cnn-selenium/scrapers.py`

**Be careful**: some script could have hardcoded parameters in them that you can tweak (e.g. the specific date you want to scrape/extract).

## Development

### On [ipython tab-completion error](https://github.com/ipython/ipython/issues/10946), use

```python
import logging

logging.getLogger('parso').setLevel(logging.WARNING)
```

### Start crawling from here: [CNN's index](https://www.cnnindonesia.com/indeks) &  [Tribun's index](https://www.tribunnews.com/index-news/news?date=2021-5-1)

### Todos

1. Make sure hardcoded date parameters are taken into account before scraping/extracting data
2. All data dump functions operate on the assumptions that the file to be dumped **does not yet exist**, so if the file *actually exist*, it will get **overwritten.** Careful handling needed

## Notes

1. Xpath descendant tags:)
   - [`//` much wow](https://stackoverflow.com/a/13490664/8996974)
2. [Two classes](https://stackoverflow.com/a/3881148/8996974)
3. [Absolute and relative paths](https://stackoverflow.com/a/35608304/8996974)
4. [Delay Download](https://stackoverflow.com/a/30410408) (mine is 1s)
5. [Don't use parse as callback because it's used internally](https://stackoverflow.com/a/32626667/8996974)
6. USE [CRAWL](https://stackoverflow.com/a/42866157/8996974) LOL
7. [Practical Decorators](https://youtu.be/MjHpMCIvwsY)
