# Глобальные классы
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# Локальные классы
from otparser import settings
from otparser.spiders.otru import OtruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    # input('')
    process.crawl(OtruSpider, query='Gigabyte')  # паук создается здесь, можем передавать множество параметров

    process.start()
