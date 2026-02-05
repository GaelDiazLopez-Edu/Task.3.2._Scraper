# Tarea 3.2: Scraper de Noticias

Este proyecto es un agregador de noticias que utiliza Scrapy para extraer información de tres medios digitales distintos. Los datos se limpian y se guardan en un único archivo JSON.

## Descripción técnica
El proyecto incluye tres spiders dentro de la misma estructura:
- El País: Utiliza selectores XPath.
- 20 Minutos: Utiliza selectores CSS.
- La Vanguardia: Utiliza selectores CSS/XPath.

Se extraen los campos de título, enlace, fuente y autor. Se ha aplicado limpieza de strings para evitar espacios en blanco innecesarios en el archivo final.

## Instrucciones de uso
Para ejecutar los spiders y acumular los resultados en el archivo de salida, se deben lanzar los siguientes comandos desde la raíz:

```bash
scrapy crawl elpais -o news_data.json
scrapy crawl venteminutos -o news_data.json
scrapy crawl lavanguardia -o news_data.json
