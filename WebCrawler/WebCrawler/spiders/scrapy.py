import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from WebCrawler.items import WebcrawlerItem
from scrapy.loader import ItemLoader
import nltk
from bs4 import BeautifulSoup


class QuotesSpider(CrawlSpider):
    name = "oizam"
    allowed_domains = ['oiseaux.net']
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.oiseaux.net/oiseaux/', headers={'User-Agent': self.user_agent})
        

    rules = (
    Rule(LinkExtractor(restrict_xpaths="//div[@class='on-pays']/div/div/a"), follow=True, process_request='set_user_agent'),
    Rule(LinkExtractor(restrict_xpaths="//*[@id='oiseaux']/div/div/div/div/table/tbody/tr/td/a"),
            callback='parse_item', follow=True, process_request='set_user_agent'),
    )


    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
    
        item = WebcrawlerItem()
        title = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/h1/span/text()").get()
        item['title'] = BeautifulSoup(title).get_text().strip()
        
        text = ''.join(Selector(response).xpath("//*[@id='description-esp']/div/p").extract()).strip()
        item['text'] = BeautifulSoup(text).get_text().strip()
        
        item['image'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div/div/div/div/figure/a/img/@src").get()
        
        item['ordre'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[2]/ul/li[1]/p/text()").get()
        item['famille'] = Selector(response).xpath('//*[@id="oiseaux"]/div/div/div[1]/div[2]/div/div[2]/ul/li[2]/text()').get()
        item['genre'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[2]/ul/li[2]/p/text()").get()
        item['espece'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[2]/ul/li[4]/p/text()").get()
        item['descripteur'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[3]/p/text()").get()
        item['taille'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[4]/ul/li[1]/text()").get()
        item['envergure'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[4]/ul/li[2]/text()").get()
        item['poids'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[4]/ul/li[3]/text()").get()
        item['localisation'] = Selector(response).xpath("//*[@id='oiseaux']/div/div/div[1]/div[2]/div/div[5]/p/img/@src").get()
        item['disparition'] = Selector(response).xpath("//span[@class='on_iucn_lc']/text()").get()
        
        yield item
        