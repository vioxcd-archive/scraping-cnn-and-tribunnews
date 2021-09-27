# Scraping CNN & Tribun

Scraping CNN using [Selenium](https://selenium-python.readthedocs.io/) & Tribun using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

The [Scrapy](https://docs.scrapy.org/en/latest/index.html) code doesn't work, idk why lol

## Run

- Create a `dump` directory on your root project
- Run `pip3 install -r requirements.txt`
- Run `python3 tribun-bs4/scrapers.py`

## Development

### On [ipython tab-completion error](https://github.com/ipython/ipython/issues/10946), use

```python
import logging

logging.getLogger('parso').setLevel(logging.WARNING)
```

### Start crawling from these links

[CNN's index](https://www.cnnindonesia.com/indeks)

[Tribun's index](https://www.tribunnews.com/index-news/news?date=2021-5-1)

### Todos

1. **important**: keep track of the titles that are overlapping between pages (on `&pages=` parameter on Tribun): some 1 May titles are included in 2 May, 2 May in 3 May, and so on. Idea: maybe create a `.csv` for all titles, loaded as `set` and check whether some of these titles are already grabbed (this might make the program runs faster)
2. uninstall scrapy related package and re-run `pip freeze`

## Notes

1. Xpath descendant tags:)
   - [`//` much wow](https://stackoverflow.com/a/13490664/8996974)
2. [Two classes](https://stackoverflow.com/a/3881148/8996974)
3. [Absolute and relative paths](https://stackoverflow.com/a/35608304/8996974)
4. [Delay Download](https://stackoverflow.com/a/30410408) (mine is 1s)
5. [Don't use parse as callback because it's used internally](https://stackoverflow.com/a/32626667/8996974)
6. USE [CRAWL](https://stackoverflow.com/a/42866157/8996974) LOL
