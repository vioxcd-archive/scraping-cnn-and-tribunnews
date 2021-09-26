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
        "https://www.tribunnews.com/index-news/news?date=2021-1-5",
        "https://www.tribunnews.com/index-news/news?date=2021-2-5",
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
        if page:
            yield scrapy.Request(next_page)
            

    def parse_article_page(self, response):
        item = {
            'title': response.xpath('//h1[@id="arttitle"]/text()').extract_first(),
            'date_published': response.xpath('//time[@class="grey"]/text()').extract_first(),
            'content': response.xpath('//div[contains(@class, "txt-article")]/p//text()').getall(),
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
        "https://www.tribunnews.com/index-news/news?date=2021-1-5",
        "https://www.tribunnews.com/index-news/news?date=2021-2-5",
        "https://www.tribunnews.com/index-news/news?date=2021-3-5",
        "https://www.tribunnews.com/index-news/news?date=2021-4-5",
        "https://www.tribunnews.com/index-news/news?date=2021-5-5",
        "https://www.tribunnews.com/index-news/news?date=2021-6-5",
        "https://www.tribunnews.com/index-news/news?date=2021-7-5",
        "https://www.tribunnews.com/index-news/news?date=2021-8-5",
        "https://www.tribunnews.com/index-news/news?date=2021-9-5",
        "https://www.tribunnews.com/index-news/news?date=2021-10-5",
        "https://www.tribunnews.com/index-news/news?date=2021-11-5",
        "https://www.tribunnews.com/index-news/news?date=2021-12-5",
        "https://www.tribunnews.com/index-news/news?date=2021-13-5",
        "https://www.tribunnews.com/index-news/news?date=2021-14-5",
        "https://www.tribunnews.com/index-news/news?date=2021-15-5",
        "https://www.tribunnews.com/index-news/news?date=2021-16-5",
        "https://www.tribunnews.com/index-news/news?date=2021-17-5",
        "https://www.tribunnews.com/index-news/news?date=2021-18-5",
        "https://www.tribunnews.com/index-news/news?date=2021-19-5",
        "https://www.tribunnews.com/index-news/news?date=2021-20-5",
        "https://www.tribunnews.com/index-news/news?date=2021-21-5",
        "https://www.tribunnews.com/index-news/news?date=2021-22-5",
        "https://www.tribunnews.com/index-news/news?date=2021-23-5",
        "https://www.tribunnews.com/index-news/news?date=2021-24-5",
        "https://www.tribunnews.com/index-news/news?date=2021-25-5",
        "https://www.tribunnews.com/index-news/news?date=2021-26-5",
        "https://www.tribunnews.com/index-news/news?date=2021-27-5",
        "https://www.tribunnews.com/index-news/news?date=2021-28-5",
        "https://www.tribunnews.com/index-news/news?date=2021-29-5",
        "https://www.tribunnews.com/index-news/news?date=2021-30-5",
        "https://www.tribunnews.com/index-news/news?date=2021-31-5",
        "https://www.tribunnews.com/index-news/news?date=2021-1-6",
        "https://www.tribunnews.com/index-news/news?date=2021-2-6",
        "https://www.tribunnews.com/index-news/news?date=2021-3-6",
        "https://www.tribunnews.com/index-news/news?date=2021-4-6",
        "https://www.tribunnews.com/index-news/news?date=2021-5-6",
        "https://www.tribunnews.com/index-news/news?date=2021-6-6",
        "https://www.tribunnews.com/index-news/news?date=2021-7-6",
        "https://www.tribunnews.com/index-news/news?date=2021-8-6",
        "https://www.tribunnews.com/index-news/news?date=2021-9-6",
        "https://www.tribunnews.com/index-news/news?date=2021-10-6",
        "https://www.tribunnews.com/index-news/news?date=2021-11-6",
        "https://www.tribunnews.com/index-news/news?date=2021-12-6",
        "https://www.tribunnews.com/index-news/news?date=2021-13-6",
        "https://www.tribunnews.com/index-news/news?date=2021-14-6",
        "https://www.tribunnews.com/index-news/news?date=2021-15-6",
        "https://www.tribunnews.com/index-news/news?date=2021-16-6",
        "https://www.tribunnews.com/index-news/news?date=2021-17-6",
        "https://www.tribunnews.com/index-news/news?date=2021-18-6",
        "https://www.tribunnews.com/index-news/news?date=2021-19-6",
        "https://www.tribunnews.com/index-news/news?date=2021-20-6",
        "https://www.tribunnews.com/index-news/news?date=2021-21-6",
        "https://www.tribunnews.com/index-news/news?date=2021-22-6",
        "https://www.tribunnews.com/index-news/news?date=2021-23-6",
        "https://www.tribunnews.com/index-news/news?date=2021-24-6",
        "https://www.tribunnews.com/index-news/news?date=2021-25-6",
        "https://www.tribunnews.com/index-news/news?date=2021-26-6",
        "https://www.tribunnews.com/index-news/news?date=2021-27-6",
        "https://www.tribunnews.com/index-news/news?date=2021-28-6",
        "https://www.tribunnews.com/index-news/news?date=2021-29-6",
        "https://www.tribunnews.com/index-news/news?date=2021-30-6",
        "https://www.tribunnews.com/index-news/news?date=2021-1-7",
        "https://www.tribunnews.com/index-news/news?date=2021-2-7",
        "https://www.tribunnews.com/index-news/news?date=2021-3-7",
        "https://www.tribunnews.com/index-news/news?date=2021-4-7",
        "https://www.tribunnews.com/index-news/news?date=2021-5-7",
        "https://www.tribunnews.com/index-news/news?date=2021-6-7",
        "https://www.tribunnews.com/index-news/news?date=2021-7-7",
        "https://www.tribunnews.com/index-news/news?date=2021-8-7",
        "https://www.tribunnews.com/index-news/news?date=2021-9-7",
        "https://www.tribunnews.com/index-news/news?date=2021-10-7",
        "https://www.tribunnews.com/index-news/news?date=2021-11-7",
        "https://www.tribunnews.com/index-news/news?date=2021-12-7",
        "https://www.tribunnews.com/index-news/news?date=2021-13-7",
        "https://www.tribunnews.com/index-news/news?date=2021-14-7",
        "https://www.tribunnews.com/index-news/news?date=2021-15-7",
        "https://www.tribunnews.com/index-news/news?date=2021-16-7",
        "https://www.tribunnews.com/index-news/news?date=2021-17-7",
        "https://www.tribunnews.com/index-news/news?date=2021-18-7",
        "https://www.tribunnews.com/index-news/news?date=2021-19-7",
        "https://www.tribunnews.com/index-news/news?date=2021-20-7",
        "https://www.tribunnews.com/index-news/news?date=2021-21-7",
        "https://www.tribunnews.com/index-news/news?date=2021-22-7",
        "https://www.tribunnews.com/index-news/news?date=2021-23-7",
        "https://www.tribunnews.com/index-news/news?date=2021-24-7",
        "https://www.tribunnews.com/index-news/news?date=2021-25-7",
        "https://www.tribunnews.com/index-news/news?date=2021-26-7",
        "https://www.tribunnews.com/index-news/news?date=2021-27-7",
        "https://www.tribunnews.com/index-news/news?date=2021-28-7",
        "https://www.tribunnews.com/index-news/news?date=2021-29-7",
        "https://www.tribunnews.com/index-news/news?date=2021-30-7",
    ]

    return urls
