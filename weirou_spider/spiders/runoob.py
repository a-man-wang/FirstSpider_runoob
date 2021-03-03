import scrapy


class RunoobSpider(scrapy.Spider):
    name = 'runoob'
    allowed_domains = ['runoob.com']
    start_urls = ['http://runoob.com/']

    def parse(self, response):

        #获取网站全部教程名称
        content_list = response.xpath('//div[@class="col middle-column-home"]/div[position()<11]')
        for i in content_list:
            name = i.xpath('./h2/text()').extract_first()
            print('-----------i am name')
            print(name)
            subname_list = i.xpath('./a')
            for subcontent in subname_list:
                subname = subcontent.xpath('./h4/text()').extract_first()
                subhref = 'http:'+ subcontent.xpath('./@href').extract_first()
                subexplain = subcontent.xpath('./strong/text()').extract_first()
                print(subname,subhref,subexplain)
                print('----------------------------')