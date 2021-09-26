import scrapy

"""
a = response.xpath('//a[contains(@href, "2021")]/@href').getall()
article_links = list(filter(lambda title: len(title) > 70, a))

# get index's next page
next_page = response.xpath('//a[contains(text(), "Next")]/@href').extract_first()

# get articles title
response.xpath('//h1[@id="arttitle"]/text()').extract_first()

# get articles published date
response.xpath('//time[@class="grey"]/text()').extract_first()

# get articles content
response.xpath('//div[contains(@class, "txt-article")]/p//text()').getall()

# get tagcloud
response.xpath('//h5[@class="tagcloud3"]/a/text()').getall()

# get article's next page
next_page = response.xpath('//div[@class="mb20"]/a/@href').extract_first()
"""

class TribunArticlesSpider(scrapy.Spider):
    name = 'tribun.articles'
    allowed_domains = ['tribunnews.com']
    # start_urls = get_urls()
    start_urls = [
        "https://www.tribunnews.com/index-news/news?date=2021-5-1",
        "https://www.tribunnews.com/index-news/news?date=2021-5-2",
    ]

    def parse(self, response):
        # get all articles links from index
        cards = response.xpath('//a[contains(@href, "2021")]/@href').getall()
        article_links = list(filter(lambda card: len(card) > 70, cards))
        
        for link in article_links:
            yield scrapy.Request(
                link,
                callback=self.parse_article_page,
            )

        # get index's next page
        next_page = response.xpath('//a[contains(text(), "Next")]/@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page)
            

    def parse_article_page(self, response):
        content = []
        content.extend(response.xpath('//div[contains(@class, "txt-article")]/p//text()').getall())

        item = {
            'title': response.xpath('//h1[@id="arttitle"]/text()').extract_first(),
            'date_published': response.xpath('//time[@class="grey"]/text()').extract_first(),
            'content': content,
            'tagcloud': response.xpath('//h5[@class="tagcloud3"]/a/text()').getall(),
        }

        # get article's next page
        next_page = response.xpath('//div[@class="mb20"]/a/@href').extract_first()

        if next_page is None:
            yield item
        else:
            yield scrapy.Request(
                next_page,
                callback=self.parse_article_next_page,
                meta={'item': item}
            )
    
    def parse_article_next_page(self, response):
        item = response.meta.get('item')
        content = response.xpath('//div[contains(@class, "txt-article")]/p//text()').getall()

        if content:
            item.update({
                'content': item['content'].extend(content)
            })

        # get article's next page again
        next_page = response.xpath('//div[@class="mb20"]/a/@href').extract_first()

        if next_page is None:
            yield item
        else:
            yield scrapy.Request(
                next_page,
                callback=self.parse_article_next_page,
                meta={'item': item}
            )


def get_urls():
    urls = [
        "https://www.tribunnews.com/index-news/news?date=2021-5-1",
        "https://www.tribunnews.com/index-news/news?date=2021-5-2",
        "https://www.tribunnews.com/index-news/news?date=2021-5-3",
        "https://www.tribunnews.com/index-news/news?date=2021-5-4",
        "https://www.tribunnews.com/index-news/news?date=2021-5-5",
        "https://www.tribunnews.com/index-news/news?date=2021-5-6",
        "https://www.tribunnews.com/index-news/news?date=2021-5-7",
        "https://www.tribunnews.com/index-news/news?date=2021-5-8",
        "https://www.tribunnews.com/index-news/news?date=2021-5-9",
        "https://www.tribunnews.com/index-news/news?date=2021-5-10",
        "https://www.tribunnews.com/index-news/news?date=2021-5-11",
        "https://www.tribunnews.com/index-news/news?date=2021-5-12",
        "https://www.tribunnews.com/index-news/news?date=2021-5-13",
        "https://www.tribunnews.com/index-news/news?date=2021-5-14",
        "https://www.tribunnews.com/index-news/news?date=2021-5-15",
        "https://www.tribunnews.com/index-news/news?date=2021-5-16",
        "https://www.tribunnews.com/index-news/news?date=2021-5-17",
        "https://www.tribunnews.com/index-news/news?date=2021-5-18",
        "https://www.tribunnews.com/index-news/news?date=2021-5-19",
        "https://www.tribunnews.com/index-news/news?date=2021-5-20",
        "https://www.tribunnews.com/index-news/news?date=2021-5-21",
        "https://www.tribunnews.com/index-news/news?date=2021-5-22",
        "https://www.tribunnews.com/index-news/news?date=2021-5-23",
        "https://www.tribunnews.com/index-news/news?date=2021-5-24",
        "https://www.tribunnews.com/index-news/news?date=2021-5-25",
        "https://www.tribunnews.com/index-news/news?date=2021-5-26",
        "https://www.tribunnews.com/index-news/news?date=2021-5-27",
        "https://www.tribunnews.com/index-news/news?date=2021-5-28",
        "https://www.tribunnews.com/index-news/news?date=2021-5-29",
        "https://www.tribunnews.com/index-news/news?date=2021-5-30",
        "https://www.tribunnews.com/index-news/news?date=2021-5-31",
        "https://www.tribunnews.com/index-news/news?date=2021-6-1",
        "https://www.tribunnews.com/index-news/news?date=2021-6-2",
        "https://www.tribunnews.com/index-news/news?date=2021-6-3",
        "https://www.tribunnews.com/index-news/news?date=2021-6-4",
        "https://www.tribunnews.com/index-news/news?date=2021-6-5",
        "https://www.tribunnews.com/index-news/news?date=2021-6-6",
        "https://www.tribunnews.com/index-news/news?date=2021-6-7",
        "https://www.tribunnews.com/index-news/news?date=2021-6-8",
        "https://www.tribunnews.com/index-news/news?date=2021-6-9",
        "https://www.tribunnews.com/index-news/news?date=2021-6-10",
        "https://www.tribunnews.com/index-news/news?date=2021-6-11",
        "https://www.tribunnews.com/index-news/news?date=2021-6-12",
        "https://www.tribunnews.com/index-news/news?date=2021-6-13",
        "https://www.tribunnews.com/index-news/news?date=2021-6-14",
        "https://www.tribunnews.com/index-news/news?date=2021-6-15",
        "https://www.tribunnews.com/index-news/news?date=2021-6-16",
        "https://www.tribunnews.com/index-news/news?date=2021-6-17",
        "https://www.tribunnews.com/index-news/news?date=2021-6-18",
        "https://www.tribunnews.com/index-news/news?date=2021-6-19",
        "https://www.tribunnews.com/index-news/news?date=2021-6-20",
        "https://www.tribunnews.com/index-news/news?date=2021-6-21",
        "https://www.tribunnews.com/index-news/news?date=2021-6-22",
        "https://www.tribunnews.com/index-news/news?date=2021-6-23",
        "https://www.tribunnews.com/index-news/news?date=2021-6-24",
        "https://www.tribunnews.com/index-news/news?date=2021-6-25",
        "https://www.tribunnews.com/index-news/news?date=2021-6-26",
        "https://www.tribunnews.com/index-news/news?date=2021-6-27",
        "https://www.tribunnews.com/index-news/news?date=2021-6-28",
        "https://www.tribunnews.com/index-news/news?date=2021-6-29",
        "https://www.tribunnews.com/index-news/news?date=2021-6-30",
        "https://www.tribunnews.com/index-news/news?date=2021-7-1",
        "https://www.tribunnews.com/index-news/news?date=2021-7-2",
        "https://www.tribunnews.com/index-news/news?date=2021-7-3",
        "https://www.tribunnews.com/index-news/news?date=2021-7-4",
        "https://www.tribunnews.com/index-news/news?date=2021-7-5",
        "https://www.tribunnews.com/index-news/news?date=2021-7-6",
        "https://www.tribunnews.com/index-news/news?date=2021-7-7",
        "https://www.tribunnews.com/index-news/news?date=2021-7-8",
        "https://www.tribunnews.com/index-news/news?date=2021-7-9",
        "https://www.tribunnews.com/index-news/news?date=2021-7-10",
        "https://www.tribunnews.com/index-news/news?date=2021-7-11",
        "https://www.tribunnews.com/index-news/news?date=2021-7-12",
        "https://www.tribunnews.com/index-news/news?date=2021-7-13",
        "https://www.tribunnews.com/index-news/news?date=2021-7-14",
        "https://www.tribunnews.com/index-news/news?date=2021-7-15",
        "https://www.tribunnews.com/index-news/news?date=2021-7-16",
        "https://www.tribunnews.com/index-news/news?date=2021-7-17",
        "https://www.tribunnews.com/index-news/news?date=2021-7-18",
        "https://www.tribunnews.com/index-news/news?date=2021-7-19",
        "https://www.tribunnews.com/index-news/news?date=2021-7-20",
        "https://www.tribunnews.com/index-news/news?date=2021-7-21",
        "https://www.tribunnews.com/index-news/news?date=2021-7-22",
        "https://www.tribunnews.com/index-news/news?date=2021-7-23",
        "https://www.tribunnews.com/index-news/news?date=2021-7-24",
        "https://www.tribunnews.com/index-news/news?date=2021-7-25",
        "https://www.tribunnews.com/index-news/news?date=2021-7-26",
        "https://www.tribunnews.com/index-news/news?date=2021-7-27",
        "https://www.tribunnews.com/index-news/news?date=2021-7-28",
        "https://www.tribunnews.com/index-news/news?date=2021-7-29",
        "https://www.tribunnews.com/index-news/news?date=2021-7-30",
    ]

    return urls
