import scrapy

class ElPaisSpider(scrapy.Spider):
    name = "elpais"
    start_urls = ["https://elpais.com/"]

    def parse(self, response):
        # Buscamos etiquetas de titular comunes en El País
        for article in response.xpath('//h2'):
            title = article.xpath('.//a/text()').get()
            link = article.xpath('.//a/@href').get()
            if title and link:
                yield {
                    'title': title.strip(), # Limpieza 
                    'link': response.urljoin(link),
                    'author': 'Redacción El País', # Campo extra 
                    'source': 'El Pais' # Identificador 
                }