# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
# from scrapy_splash import SplashRequest

class Quote(scrapy.Spider):
    name = 'quote'
    # def start_requests(self):
    #     yield start_requests (
    #         url='https://www.tripadvisor.com.vn/Restaurant_Review-g293924-d12907802-Reviews-Kebab_Co-Hanoi.html',
    #         callback=self.parse,
    #     )
    start_urls = [
        'https://www.tripadvisor.com/Hotel_Review-g150812-d2064902-Reviews-or7195-Paradisus_Playa_del_Carmen_La_Perla-Playa_del_Carmen_Yucatan_Peninsula.html'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome("/home/gvt/Desktop/chromedriver")

    def parse(self, response):
        next = response.xpath(
            '//div[@class="listContainer hide-more-mobile"]/div[@class="mobile-more"]/div[@class="prw_rup prw_common_responsive_pagination"]/div/a[2]/@href').extract_first()
        next_page = 'https://www.tripadvisor.com' + next
        if next is not None:
            self.driver.get(response.request.url)
            while True:
                try:
                    next = self.driver.find_element_by_xpath(
                        '//div[@class="review-container"]/div/div/div/div/div[@class="prw_rup prw_reviews_text_summary_hsx"]/div/p/span[contains(text(),"More")]')
                    next.click()
                    time.sleep(1)
                    for quote in self.driver.find_elements_by_xpath('//div[@class="review-container"]'):
                        yield {
                            'rating':
                                quote.find_element_by_class_name('ui_bubble_rating').get_attribute('class').split(' ')[
                                    1].replace('bubble_', ''),
                            'noQuotes': quote.find_element_by_class_name('noQuotes').text,
                            'partial_entry': quote.find_element_by_class_name('partial_entry').text,
                        }
                    yield scrapy.Request(next_page, callback=self.parse)
                except:
                    break
        else:
            self.driver.close()




    # def parse2(self, response):
    #     for quote in response.xpath('//div[@class="review-container"]'):
    #         yield {
    #             'noQuotes': quote.xpath('.//span[@class="noQuotes"]/text()').extract_first(),
    #             'partial_entry': quote.xpath('.//p[@class="partial_entry"]/text()').extract_first(),
    #         }
        # next_page_xxx = response.xpath(
        #     '//div[@class="listContainer hide-more-mobile"]/div[@class="mobile-more"]/div[@class="prw_rup prw_common_responsive_pagination"]/div/a[2]/@href').extract_first()
        # if next_page_xxx is not None:
        #     next_page = 'https://www.tripadvisor.com' + next_page_xxx
        #     yield scrapy.Request(next_page_xxx, callback=self.parse)
        # else:
        #     self.driver.close()

    # def parse(self, response):
    #     yield {
    #         'more': response.xpath('//div[@class="review-container"]/div/div/div/div/div[@class="prw_rup prw_reviews_text_summary_hsx"]/div/p/span[contains(text(),"More")]/@class').extract_first(),
    #     }
        # for quote in response.xpath('//div[@class="review-container"]'):
        #     yield {
        #         'noQuotes': quote.xpath('.//span[@class="noQuotes"]/text()').extract_first(),
        #         'partial_entry': quote.xpath('.//p[@class="partial_entry"]/text()').extract_first(),
        #     }
        # next_page = response.xpath('//div[@class="listContainer hide-more-mobile"]/div[@class="mobile-more"]/div[@class="prw_rup prw_common_responsive_pagination"]/div/a[2]/@href').extract_first()
        # if next_page is not None:
        #     next_page = 'https://www.tripadvisor.com' + next_page
        #     yield scrapy.Request(next_page, callback=self.parse)
