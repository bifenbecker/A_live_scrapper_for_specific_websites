import json, requests, re
from bs4 import BeautifulSoup
from ExceptionBreak import ExceptionBreak

class IPhone12proMax:
    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    # Brand new

    websites = {
        'OnBuy128':'https://www.onbuy.com/gb/unlocked-128gb-apple-iphone-12-pro-max-dual-sim-silver~c12871~p26038787/',
        'ebay128':'https://www.ebay.co.uk/p/6041725460?iid=264998085506',
        'CarphoneWarehouse128':'https://www.carphonewarehouse.com/apple/iphone-12-pro-max.html#!colour=silver&capacity=128GB&dealType=sf',
        'Apple128':'https://www.apple.com/uk/shop/buy-iphone/iphone-12-pro',
        'JohnLewis128':'https://www.johnlewis.com/apple-iphone-12-pro-max-ios-6-7-inch-5g-sim-free-128gb/graphite/p5178112',

        'Apple256':'https://www.apple.com/uk/shop/buy-iphone/iphone-12-pro',
        'ebay256':'https://www.ebay.co.uk/p/17041715571?iid=264999262079&thm=4000',
        'JohnLewis256':'https://www.johnlewis.com/apple-iphone-12-pro-max-ios-6-7-inch-5g-sim-free-256gb/silver/p5178113',
        'CarphoneWarehouse256':'https://www.carphonewarehouse.com/apple/iphone-12-pro-max.html#!colour=silver&capacity=256GB&dealType=sf',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-12-pro-max-dual-sim-gold~c12871~p26039516/',
        'vendi256':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+12+pro+max+256',

        'CarphoneWarehouse512':'https://www.carphonewarehouse.com/apple/iphone-12-pro-max.html#!colour=silver&capacity=512GB&dealType=sf',
        'Apple512':'https://www.apple.com/uk/shop/buy-iphone/iphone-12-pro',
        'OnBuy512':'https://www.onbuy.com/gb/unlocked-512gb-apple-iphone-12-pro-max-dual-sim-graphite~c12871~p26039123/',

    }

    def getListPrice_BrandNew(self):
        l = [
            self.getPrice_OnBuy_128gb(),
            self.getPrice_ebay_128gb(),
            self.getPrice_CarphoneWarehouse_128gb(),
            self.getPrice_Apple_128gb(),
            self.getPrice_JohnLewis_128gb(),
            self.getPrice_Apple_256gb(),
            self.getPrice_ebay_256gb(),
            self.getPrice_JohnLewis_256gb(),
            self.getPrice_CarphoneWarehouse_256gb(),
            self.getPrice_OnBuy_256gb(),
            self.getPrice_vendi_256gb(),
            self.getPrice_CarphoneWarehouse_512gb(),
            self.getPrice_Apple_512gb(),
            self.getPrice_OnBuy_512gb(),

        ]
        #return list(map(lambda x: float(x[1:].replace(',', '.')), l))
        return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))

    def getData_BrandNew(self):
        colors = ['Graphite', 'Silver', 'Gold', 'Pacific blue']
        IPhones = []
        try:
            prices = self.getListPrice_BrandNew()
        except:
            raise ExceptionBreak("Error in Iphone 12 pro max")
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone12proMax',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones


    def getPrice_CarphoneWarehouse_512gb(self):
        url = self.websites['CarphoneWarehouse512']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-silver-512gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-pacificblue-512gb']

    def getPrice_Apple_512gb(self):
        url = self.websites['Apple512']
        return self.get_soap(url).find_all('span', class_='current_price')[20].text.replace(',','')

    def getPrice_OnBuy_512gb(self):
        url = self.websites['OnBuy512']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')



    def getPrice_Apple_256gb(self):
        url = self.websites['Apple256']
        return self.get_soap(url).find_all('span', class_='current_price')[16].text.replace(',','')

    def getPrice_ebay_256gb(self):
        url = self.websites['ebay256']
        return self.get_soap(url).find('div', class_ = 'display-price').text.replace(',','')

    def getPrice_JohnLewis_256gb(self):
        url = self.websites['JohnLewis256']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','').replace(',','')

    def getPrice_CarphoneWarehouse_256gb(self):
        url = self.websites['CarphoneWarehouse256']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-silver-256gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-pacificblue-256gb']

    def getPrice_OnBuy_256gb(self):
        url = self.websites['OnBuy256']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')

    def getPrice_vendi_256gb(self):
        url = self.websites['vendi256']
        if len(self.get_soap(url).find_all('span', class_ = 'price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_ = 'price')[0].text.replace(',','').split('£')[-1]
        else:
            return self.getPrice_Apple_256gb()

    def getPrice_OnBuy_128gb(self):
        url = self.websites['OnBuy128']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')

    def getPrice_ebay_128gb(self):
        url = self.websites['ebay128']
        return self.get_soap(url).find('div', class_ = 'display-price').text

    def getPrice_CarphoneWarehouse_128gb(self):
        url = self.websites['CarphoneWarehouse128']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-silver-128gb']
        except:
            return '£1099'

    def getPrice_Apple_128gb(self):
        url = self.websites['Apple128']
        return self.get_soap(url).find_all('span', class_='current_price')[12].text.replace(',','')

    def getPrice_JohnLewis_128gb(self):
        url = self.websites['JohnLewis128']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','').replace(',','')
