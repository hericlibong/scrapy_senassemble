import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AssemblecrawlSpider(CrawlSpider):
    name = 'assemblecrawl'
    allowed_domains = ['assemblee-nationale.sn']
    start_urls = ['http://www.assemblee-nationale.sn/deputes-de-l-hemicycle-1-all.xml?p=active7#']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//table[@class='table table-bordered table-striped']//td//following-sibling::node()/a"), callback='parse_item', follow= True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']//a[1]")),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']//a[2]")),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']//a[3]")),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']//a[4]")),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']//a[5]")),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination']//a[6]")),
        
        
        
    )

    def parse_item(self, response):
        name = response.xpath("//li[@class='img']/h3/text()").get()
        circonscription = response.xpath("//li[@class='img']/p/text()").get().replace('Député département de ', '')
        coalition = response.xpath("normalize-space(//h4/text())").get().strip('/').strip(':').strip()
        image =  response.xpath("//li[@class='img']/img/@src").get()
            
    
        results = {
            'name':name,
            'circonscription':circonscription,
            'coalition':coalition,
            'image_url': f'http://www.assemblee-nationale.sn/{image}'
            }
        yield results
