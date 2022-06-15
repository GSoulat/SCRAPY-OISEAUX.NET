# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import WebCrawler.WebCrawler.spiders.scrapy as scrapy
import scrapy

class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    text = scrapy.Field()
    image = scrapy.Field()
    ordre = scrapy.Field()
    famille = scrapy.Field()
    genre = scrapy.Field()
    espece = scrapy.Field()
    descripteur  = scrapy.Field()
    taille   = scrapy.Field()
    envergure   = scrapy.Field()
    poids   = scrapy.Field()
    localisation   = scrapy.Field()
    disparition = scrapy.Field()
    
    pass
