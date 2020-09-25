#####
####login to github
####
import scrapy
from scrapy.utils.response import open_in_browser
class TestloginSpider(scrapy.Spider):
    name = 'testlogin'
    start_urls = ['https://github.com/login']
    headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51x-requested-with: XMLHttpRequest',
            }

    def parse(self, response):
        hiden_items=response.css('input[type="hidden"]::attr(value) ').getall()
        formdata={
                    'commit': 'Sign in',
                    'authenticity_token': hiden_items[0],
                    'ga_id': '',
                    'login': 'mzahhd@gmail.com',
                    'password': '123485',
                    'webauthn-support': 'supported',
                    'webauthn-iuvpaa-support': 'unsupported',
                    'return_to': '',
                    'required_field_cd8a': '',
                    'timestamp': hiden_items[-2],
                    'timestamp_secret': hiden_items[-1],
        }

        yield scrapy.FormRequest(url=self.start_urls[0],method='POST',formdata=formdata, headers=self.headers,callback=self.parse_test,errback=self.errback)
        print("######################################################################################################################################################")


    def parse_test(self, response):
        print('*************************************************************************test*************************************************************************')
        response.follow('https://github.com/')
        print("######################################################################################################################################################")
        print("######################################################################################################################################################")
        print("######################################################################################################################################################")
        print("######################################################################################################################################################")
        yield response.css('body::text').get()
        print("######################################################################################################################################################")
        print("######################################################################################################################################################")
        print("######################################################################################################################################################")
        print("######################################################################################################################################################")

        #open_in_browser(response)
	    # print (response.css('#user_tag::text').get())
    def errback(self,response):
        print('*******************************************************************')
        print('****************************** error ******************************')
        print('*******************************************************************')