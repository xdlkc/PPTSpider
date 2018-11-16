# -*- coding: utf-8 -*-
import scrapy
from PPTSpider.items import FileDownloadItem
import requests
from PPTSpider.utils import file_util


class OnepptspiderSpider(scrapy.Spider):
    name = 'OnePptSpider'
    allowed_domains = ['http://www.1ppt.com', 'http://ppt.1ppt.com']
    start_urls = []
    index_url = 'http://www.1ppt.com/'

    def __init__(self, **kwargs):
        """
        moban:114
        beijing:58
        :param kwargs:
        """
        super().__init__(**kwargs)
        moban_url = 'http://www.1ppt.com/moban/ppt_moban_{}.html'
        sucai_url = 'http://www.1ppt.com/sucai/ppt_sucai_{}.html'
        tubiao_url = 'http://www.1ppt.com/tubiao/ppt_tubiao_{}.html'
        beijing_url = 'http://www.1ppt.com/beijing/ppt_beijing_{}.html'
        count = 58
        for i in range(1, count):
            self.start_urls.append(beijing_url.format(i))

    def parse(self, response):
        tplist = response.xpath('//ul[@class="tplist"]')
        for tpli in tplist.xpath('./li'):
            url = "{}{}".format(self.index_url, tpli.xpath('./a/@href')[0].extract())
            yield scrapy.Request(url=url, callback=self.parse_article, dont_filter=True)

    def parse_article(self, response):
        downlist = response.xpath('//ul[@class="downurllist"]')[0]
        file_url = downlist.xpath('.//a/@href').extract()[0]
        name = response.xpath('//div[@class="ppt_info clearfix"]/h1/text()').extract()[0]
        res = requests.get(file_url)
        file_type = self.judge_type(file_url.split('.'))
        file_name = '/Users/zhangjunbo/Documents/ppt/beijing/{}.{}'.format(name, file_type)
        output = open(file_name, 'wb')
        output.write(res.content)
        output.close()
        if file_type is 'rar':
            file_util.un_rar(file_name)
        elif file_type is 'zip':
            file_util.un_zip(file_name)

    def judge_type(self, name):
        if 'rar' in name:
            return 'rar'
        elif 'zip' in name:
            return 'zip'
        return 'zip'
