import scrapy

class LaVanguardiaSpider(scrapy.Spider):
    name = "lavanguardia"
    start_urls = ["https://www.lavanguardia.com/"]

    def parse(self, response):
        for article in response.css('article'):
            title = article.css('h1 a::text, h2 a::text, h3 a::text').get()
            if title:
                yield {
                    'title': title.strip(), # Limpieza [cite: 133]
                    'link': response.urljoin(article.css('a::attr(href)').get()),
                    'source': 'La Vanguardia' # Identificador [cite: 134]
                }