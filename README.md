# Scraping CNN & Tribun

Scraping CNN using [Selenium](https://selenium-python.readthedocs.io/) & Tribun using [Scrapy](https://docs.scrapy.org/en/latest/index.html)

## Development

### On [ipython tab-completion error](https://github.com/ipython/ipython/issues/10946), use

```python
import logging

logging.getLogger('parso').setLevel(logging.WARNING)
```

### Start crawling from these links

[CNN's index](https://www.cnnindonesia.com/indeks)

[Tribun's index](https://www.tribunnews.com/index-news/news?date=2021-5-1)

### [To get your output, run it like this:](https://stackoverflow.com/a/57054297/8996974)

`scrapy runspider tribun_articles.py -o tribun_articles.json`

## Notes

1. Xpath descendant tags:)
   - [`//` much wow](https://stackoverflow.com/a/13490664/8996974)
2. [Two classes](https://stackoverflow.com/a/3881148/8996974)
3. [Absolute and relative paths](https://stackoverflow.com/a/35608304/8996974)
4. [Delay Download](https://stackoverflow.com/a/30410408) (mine is 1s)
