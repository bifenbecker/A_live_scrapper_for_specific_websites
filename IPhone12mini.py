import json, requests, re
from bs4 import BeautifulSoup
from ExceptionBreak import ExceptionBreak

class IPhone12mini:

    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    # Brand new
    websites = {
        'vendi64':'https://shop.vendiapp.com/products/apple-iphone-12-mini-64gb-6?_pos=1&_sid=5c1f99dd1&_ss=r',
        'Amazon64':'https://www.amazon.co.uk/New-Apple-iPhone-mini-64GB/dp/B08L5RDCZZ/ref=redir_mobile_desktop?ie=UTF8&aaxitk=PeCV68rJwh01BsVwA2kAiA&hsa_cr_id=3382607550302&ref_=sbx_be_s_sparkle_td_asin_0',
        'GiffGaff64':'https://www.giffgaff.com/mobile-phones/apple/iphone-12-mini-5g/new',
        'JohnLewis64':'https://www.johnlewis.com/apple-iphone-12-mini-ios-5-4-inch-5g-sim-free-64gb/black/p5178115',
        'CurrysPc64':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-mini-64-gb-black-10215578-pdt.html',
        'CarphoneWarehouse64':'https://www.carphonewarehouse.com/apple/iphone-12-mini.html#!colour=black&capacity=64GB&dealType=sf',
        'OnBuy64':'https://www.onbuy.com/gb/apple-iphone-12-mini-dual-sim-white~c12871~p26038650/',
        'Apple64':'https://www.apple.com/uk/shop/buy-iphone/iphone-12',
        'Argos64':'https://www.argos.co.uk/product/8482967?clickSR=slp:term:iphone%2012%20mini:1:127:1',
        'OnBuy128':'https://www.onbuy.com/gb/unlocked-128gb-apple-iphone-12-mini-dual-sim-white~c12871~p26038666/',
        'Amazon128':'https://www.amazon.co.uk/New-Apple-iPhone-mini-64GB/dp/B08L5PBXPR/ref=redir_mobile_desktop?ie=UTF8&aaxitk=PeCV68rJwh01BsVwA2kAiA&hsa_cr_id=3382607550302&ref_=sbx_be_s_sparkle_td_asin_0&th=1',
        'CurrysPc128':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-mini-128-gb-black-10215584-pdt.html',
        'GiffGaff128':'https://www.giffgaff.com/mobile-phones/apple/iphone-12-mini-5g/new',
        'CarphoneWarehouse128':'https://www.carphonewarehouse.com/apple/iphone-12-mini.html#!colour=black&capacity=128GB&dealType=sf',
        'vendi128':'https://shop.vendiapp.com/products/apple-iphone-12-mini-128gb-2?_pos=1&_sid=f4e1dfac7&_ss=r',
        'Apple128':'https://www.apple.com/uk/shop/buy-iphone/iphone-12',
        'Argos128':'https://www.argos.co.uk/product/8483382?clickSR=slp:term:iphone%2012%20mini:2:127:1',
        'CurrysPc256':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-mini-256-gb-black-10215590-pdt.html',
        'JohnLewis256':'https://www.johnlewis.com/apple-iphone-12-mini-ios-5-4-inch-5g-sim-free-256gb/black/p5178117',
        'CarphoneWarehouse256':'https://www.carphonewarehouse.com/apple/iphone-12-mini.html#!colour=black&capacity=256GB&dealType=sf',
        'GiffGaff256':'https://www.giffgaff.com/mobile-phones/apple/iphone-12-mini-5g/new',
        'Amazon256':'https://www.amazon.co.uk/New-Apple-iPhone-mini-64GB/dp/B08L5RHK7T/ref=redir_mobile_desktop?ie=UTF8&aaxitk=PeCV68rJwh01BsVwA2kAiA&hsa_cr_id=3382607550302&ref_=sbx_be_s_sparkle_td_asin_0&th=1',
        'Apple256':'https://www.apple.com/uk/shop/buy-iphone/iphone-12',
        'Argos256':'https://www.argos.co.uk/product/8483643?clickSR=slp:term:iphone%2012%20mini:6:127:1',
        'ebay256':'https://www.ebay.co.uk/itm/Apple-iPhone-12-Mini-5G-Unlocked-Smartphone-5-4-256GB-Dual-Camera-Face-ID/274621038030?epid=21041715493&hash=item3ff0b07dce%3Ag%3ArbcAAOSw-tBf4Lsi&LH_BIN=1&LH_ItemCondition=1000',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-12-mini-dual-sim-white~c12871~p26038675/',

    }

    def getListPrice(self):
        l = [
            self.getPrice_vendi_64gb(),
            self.getPrice_Amazon_64gb(),
            self.getPrice_GiffGaff_64gb(),
            self.getPrice_JohnLewis_64gb(),
            self.getPrice_CurrysPc_64gb(),
            self.getPrice_CarphoneWarehouse_64gb(),
            self.getPrice_OnBuy_64gb(),
            self.getPrice_Apple_64gb(),
            self.getPrice_Argos_64gb(),
            self.getPrice_OnBuy128gb(),
            self.getPrice_Amazon_128gb(),
            self.getPrice_CurrysPc_128gb(),
            self.getPrice_GiffGaff_128gb(),
            self.getPrice_CarphoneWarehouse_128gb(),
            self.getPrice_vendi_128gb(),
            self.getPrice_Apple_128gb(),
            self.getPrice_Argos_128gb(),
            self.getPrice_CurrysPc_256gb(),
            self.getPrice_JohnLewis_256gb(),
            self.getPrice_CarphoneWarehouse_256gb(),
            self.getPrice_GiffGaff_256gb(),
            self.getPrice_Amazon_256gb(),
            self.getPrice_Apple_256gb(),
            self.getPrice_Argos_256gb(),
            self.getPrice_ebay_256gb(),
            self.getPrice_OnBuy_256gb(),
        ]
        try:
            return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', x)[0]), l))
        except:
            print("Error Iphone12mini")


    def getData_BrandNew(self):
        colors = ['White', 'Black', 'Blue', 'Green','Red']
        IPhones = []
        try:
            prices = self.getListPrice()
        except:
            raise ExceptionBreak("Error in Iphone 12 mini")
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone12mini',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    def getPrice_vendi_64gb(self):
        url = self.websites['vendi64']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text))

    def getPrice_Amazon_64gb(self):
        return '£679'

    def getPrice_GiffGaff_64gb(self):
        return '£679'

    def getPrice_JohnLewis_64gb(self):
        url = self.websites['JohnLewis64']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')

    def getPrice_CurrysPc_64gb(self):
        url = self.websites['CurrysPc64']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_CarphoneWarehouse_64gb(self):
        url = self.websites['CarphoneWarehouse64']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-black-64gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-blue-64gb']

    def getPrice_OnBuy_64gb(self):
        url = self.websites['OnBuy64']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_Apple_64gb(self):
        url = self.websites['Apple64']
        return self.get_soap(url).find_all('span', class_='current_price')[0].text

    def getPrice_Argos_64gb(self):
        return '£699.00'

    def getPrice_OnBuy128gb(self):
        url = self.websites['OnBuy128']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_Amazon_128gb(self):
        return '£729'

    def getPrice_CurrysPc_128gb(self):
        url = self.websites['CurrysPc128']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_GiffGaff_128gb(self):
        return '£749'

    def getPrice_CarphoneWarehouse_128gb(self):
        url = self.websites['CarphoneWarehouse128']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-black-128gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-blue-128gb']

    def getPrice_vendi_128gb(self):
        url = self.websites['vendi128']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text))

    def getPrice_Apple_128gb(self):
        url = self.websites['Apple128']
        return self.get_soap(url).find_all('span', class_='current_price')[5].text

    def getPrice_Argos_128gb(self):
        return '£749.00'

    def getPrice_CurrysPc_256gb(self):
        url = self.websites['CurrysPc256']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_JohnLewis_256gb(self):
        url = self.websites['JohnLewis256']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')

    def getPrice_CarphoneWarehouse_256gb(self):
        url = self.websites['CarphoneWarehouse256']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-black-256gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-blue-256gb']

    def getPrice_GiffGaff_256gb(self):
        return '£849'

    def getPrice_Amazon_256gb(self):
        return '£849'

    def getPrice_Apple_256gb(self):
        url = self.websites['Apple256']
        return self.get_soap(url).find_all('span', class_='current_price')[10].text

    def getPrice_Argos_256gb(self):
        return '£849.00'

    def getPrice_ebay_256gb(self):
        url = self.websites['ebay256']
        return self.get_soap(url).find('span', id='prcIsum').text

    def getPrice_OnBuy_256gb(self):
        url = self.websites['OnBuy256']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')




















