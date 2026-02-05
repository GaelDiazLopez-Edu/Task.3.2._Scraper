import scrapy

class VenteMinutosSpider(scrapy.Spider):
    name = "venteminutos"
    start_urls = ["https://www.20minutos.es/"]

    def parse(self, response):
        for article in response.css('article'):
            title = article.css('h1 a::text, h2 a::text').get()
            if title:
                yield {
                    'title': title.strip(), # Limpieza [cite: 133]
                    'link': article.css('h1 a::attr(href), h2 a::attr(href)').get(),
                    'source': '20minutos' # Identificador [cite: 134]
                }