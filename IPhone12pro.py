import json, requests, re
from bs4 import BeautifulSoup

class IPhone12pro:

    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    #Brand new

    websites = {
        'Argos128':'https://www.argos.co.uk/product/8480653',
        'CurrysPc128':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-pro-128-gb-graphite-10215619-pdt.html',
        'CarphoneWarehouse128':'https://www.carphonewarehouse.com/apple/iphone-12-pro.html#!colour=graphite&capacity=128GB&dealType=sf',
        'JohnLewis128':'https://www.johnlewis.com/apple-iphone-12-pro-ios-6-1-inch-5g-sim-free-128gb/graphite/p5178100',
        'Apple128':'https://www.apple.com/uk/shop/buy-iphone/iphone-12-pro',
        'ebay128':'https://www.ebay.co.uk/p/3041720574?iid=264988946629',
        'vendi128':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+12+128gb',
        'Argos256':'https://www.argos.co.uk/product/8480835?clickSR=slp:term:12%20pro:11:64:1',
        'JohnLewis256':'https://www.johnlewis.com/apple-iphone-12-pro-ios-6-1-inch-5g-sim-free-256gb/graphite/p5178110',
        'Apple256':'https://www.apple.com/uk/shop/buy-iphone/iphone-12-pro',
        'CurrysPc256':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-pro-256-gb-graphite-10215623-pdt.html',
        'CarephoneWarehouse256':'https://www.carphonewarehouse.com/apple/iphone-12-pro.html#!colour=graphite&capacity=256GB&dealType=sf',
        'OnBuy128':'https://www.onbuy.com/gb/unlocked-128gb-apple-iphone-12-pro-dual-sim-gold~c12871~p26040070/',
        'ebay256':'https://www.ebay.co.uk/p/23041723757?iid=284130956276',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-12-pro-dual-sim-graphite~c12871~p26039600/',
        'Apple512':'https://www.apple.com/uk/shop/buy-iphone/iphone-12-pro',
        'CurrysPc512':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-pro-512-gb-graphite-10215615-pdt.html',
        'JohnLewis512':'https://www.johnlewis.com/apple-iphone-12-pro-ios-6-1-inch-5g-sim-free-512gb/graphite/p5178111',
        'Argos512':'https://www.argos.co.uk/product/8481322?clickSR=slp:term:12%20pro:14:64:1',
        'CarphoneWarehouse512':'https://www.carphonewarehouse.com/apple/iphone-12-pro.html#!colour=graphite&capacity=512GB&dealType=sf',

    }

    def getListPrice(self):
        l = [
            self.getPrice_Argos_128gb(),
            self.getPrice_CurrysPc_128gb(),
            self.getPrice_CarphoneWarehouse_128gb(),
            self.getPrice_JohnLewis_128gb(),
            self.getPrice_Apple_128gb(),
            self.getPrice_ebay_128gb(),
            self.getPrice_vendi_128gb(),
            self.getPrice_Argos_256gb(),
            self.getPrice_JohnLewis_256gb(),
            self.getPrice_Apple_256gb(),
            self.getPrice_CurrysPc_256gb(),
            self.getPrice_CarphoneWarehouse_256gb(),
            self.getPrice_OnBuy_128gb(),
            self.getPrice_ebay_256gb(),
            self.getPrice_OnBuy_256gb(),
            self.getPrice_Apple_512gb(),
            self.getPrice_CurrysPc_512gb(),
            self.getPrice_JohnLewis_512gb(),
            self.getPrice_Argos_512gb(),
            self.getPrice_CarphoneWarehouse_512gb(),
        ]

        return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))


    def getData_BrandNew(self):
        colors = ['Graphite', 'Silver', 'Gold', 'Pacific Blue']
        IPhones = []
        prices = self.getListPrice()

        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone12pro',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones



    def getPrice_Argos_128gb(self):
        url = self.websites['Argos128']
        return '£999.00'

    def getPrice_CurrysPc_128gb(self):
        url = self.websites['CurrysPc128']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_CarphoneWarehouse_128gb(self):
        url = self.websites['CarphoneWarehouse128']
        return '£' + self.get_soap(url).find('span', id = 'upfrontCostDo')['data-gold-128gb']

    def getPrice_JohnLewis_128gb(self):
        url = self.websites['JohnLewis128']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')

    def getPrice_Apple_128gb(self):
        url = self.websites['Apple128']
        return self.get_soap(url).find_all('span', class_='current_price')[1].text

    def getPrice_ebay_128gb(self):
        url = self.websites['ebay128']
        return self.get_soap(url).find('div', class_ = 'display-price').text

    def getPrice_vendi_128gb(self):
        url = self.websites['vendi128']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[0].text.replace(',', '').split('£')[-1]
        else:
            return '£820'


    def getPrice_Argos_256gb(self):
        return '£1099.00'

    def getPrice_JohnLewis_256gb(self):
        url = self.websites['JohnLewis256']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ', '').replace('\n', '')

    def getPrice_Apple_256gb(self):
        url = self.websites['Apple256']
        return self.get_soap(url).find_all('span', class_='current_price')[4].text

    def getPrice_CurrysPc_256gb(self):
        url = self.websites['CurrysPc256']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_CarphoneWarehouse_256gb(self):
        url = self.websites['CarephoneWarehouse256']
        return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-gold-256gb']

    def getPrice_OnBuy_128gb(self):
        url = self.websites['OnBuy128']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_ebay_256gb(self):
        url = self.websites['ebay256']
        return self.get_soap(url).find('div', class_='display-price').text

    def getPrice_OnBuy_256gb(self):
        url = self.websites['OnBuy256']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_Apple_512gb(self):
        url = self.websites['Apple512']
        return self.get_soap(url).find_all('span', class_='current_price')[8].text

    def getPrice_CurrysPc_512gb(self):
        url = self.websites['CurrysPc512']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_JohnLewis_512gb(self):
        url = self.websites['JohnLewis512']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ', '').replace('\n', '')

    def getPrice_Argos_512gb(self):
        url = self.websites['Argos512']
        return '£1299.00'

    def getPrice_CarphoneWarehouse_512gb(self):
        url = self.websites['CarphoneWarehouse512']
        return '£' + self.get_soap(url).find('span', id = 'upfrontCostDo')['data-gold-512gb']