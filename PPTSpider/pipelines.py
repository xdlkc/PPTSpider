# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy
import os

class PptspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class FileDownloadPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        print("sdadad")
        for url in item["file_url"]:
            print("sdadad")
            yield scrapy.Request(url)

    def file_path(self, request, response=None, info=None):
        """
        重命名模块
        """
        print("sadadsad")
        path = os.path.join('/Users/zhangjunbo/Documents/ppt', ''.join(
            [request.url.replace('//', '_').replace('/', '_').replace(':', '_').replace('.', '_').replace('__', '_'),
             '.zip']))
        return path
