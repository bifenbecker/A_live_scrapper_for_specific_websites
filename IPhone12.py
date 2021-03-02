import json, requests, re
from bs4 import BeautifulSoup
from ExceptionBreak import ExceptionBreak

class IPhone12:
    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    # Brand new

    websites = {
        'vendi64':'https://shop.vendiapp.com/products/apple-iphone-12-64gb-5?_pos=3&_sid=c38d02e74&_ss=r',
        'ebay64':'https://www.ebay.co.uk/itm/NEW-SEALED-Apple-iPhone-12-64GB-A2403-BLACK-UNLOCKED-1-YEAR-APPLE-WARRANTY/264958614810?epid=5041723784&_trkparms=ispr%3D1&hash=item3db0c39d1a%3Ag%3AFNkAAOSw%7EJhfs51s&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkXKoKcbeZcOrOku%252BoOBl%252BS5oKIDzc2FZlgSj1U%252Fc7uOP5L8ioJj%252B086zkf3qmNg3kIwk6wDLJfuBHXlxlmCytB4Jvd%252B2FhmChkIG9%252BZBoBQwjizgseFwFkKI9UGgUeJOUiBK0my8cBkBBE7ucLaKd97w7PjxJNJRt0ilGdXy4MKPUVov6djT4dKGpDgWAWABDv7L1b1UOca7tkum9JcsckOmuOZ18NAOg3Uw%252Fq7k2QYj9Q9M33no6f87XXdMikqRBSHrHEoPbFT3dEXCkFY4h5pWY4PUC8k4heVqFcqabOw2VG9wGivMKcgtS958eNnwNTLJwwjyuKDs10UO4I1Cn2wZ7aXrMMWJLMbxOLmBQjqTOD3%252BqUw%252BYP8kbRUaA%252Bs0jYXUgHx1mp8pjLROjv9HptaohjhABzpR7y7j6qfq2jXo3Ct4B5ERHGatwfCQpXYlwNa%252FEaTtuxrAkMRsUKvUo40v9TOTP4xJ1TTOG%252FKQzE3ZkeVnqmerKLvQa1SEwzMQLi0O5nYt2UHtUEn4M0j51%252FH%252FpBamwgPvrW9PQiz23tDjOFOvz0fPv1d%252B96Lp5thp5Al%252FuNwEQ4D8%252BGWKv%252BHrpYRCRFzcJcKAUYZPQBBPe%252BDPf5X2UdMt%252FkhCqOb1VIxwFBlaBNOTfXYXBL3OGymjmqHGRtsqjxUZz2XINcyd6XQamnU%252BMVESZVC38or%252BmLTYqhc72Rh3je1KlWV72no%252BSP7IIT6D3pRchU3j4Ofl74UpmLbe5n0qsMnmmhfljL14zaDC1UiYRbbquIpTkpR%252BEMw%253D%253D%7Ccksum%3A264958614810c188992c81e64414a2ef7b7448a7e97e%7Campid%3APL_CLK%7Cclp%3A2334524&LH_ItemCondition=1000',
        'GiffGaff64':'https://www.giffgaff.com/mobile-phones/apple/iphone-12-5g/new',
        'CarphoneWarehouse64':'https://www.carphonewarehouse.com/apple/iphone-12.html#!colour=black&capacity=64GB&dealType=sf',
        'Argos64':'https://www.argos.co.uk/product/8469959?clickSR=slp:term:iphone%2012:1:94:1',
        'JohnLewis64':'https://www.johnlewis.com/apple-iphone-12-ios-6-1-inch-5g-sim-free-64gb/black/p5178118',
        'Amazon64':'https://www.amazon.co.uk/New-Apple-iPhone-12-128GB/dp/B08L5Q35WQ/ref=sr_1_1_sspa?dchild=1&keywords=iphone%2B12&qid=1609334864&quartzVehicle=93-1814&replacementKeywords=iphone&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQVVBQUxQWVA2QldWJmVuY3J5cHRlZElkPUEwNTg3MjkyMlhWNE8zVEtWSkQ1UCZlbmNyeXB0ZWRBZElkPUEwMDQxMTE5MjBRWlI5VDE5QVg2NyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1',
        'Apple64':'https://www.apple.com/uk/shop/buy-iphone/iphone-12',
        'CurrysPc64':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-64-gb-black-10215596-pdt.html',

        'vendi128':'https://shop.vendiapp.com/products/apple-iphone-12-128gb-11?_pos=1&_sid=3972c3f64&_ss=r',
        'OnBuy128':'https://www.onbuy.com/gb/unlocked-64gb-apple-iphone-12-dual-sim-black~c12871~p26038713/',
        'ebay128':'https://www.ebay.co.uk/p/2312761123?iid=264963667050',
        'Amazon128':'https://www.amazon.co.uk/New-Apple-iPhone-12-128GB/dp/B08L5PX5QX/ref=sr_1_1_sspa?dchild=1&keywords=iphone%2B12&qid=1609334864&quartzVehicle=93-1814&replacementKeywords=iphone&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQVVBQUxQWVA2QldWJmVuY3J5cHRlZElkPUEwNTg3MjkyMlhWNE8zVEtWSkQ1UCZlbmNyeXB0ZWRBZElkPUEwMDQxMTE5MjBRWlI5VDE5QVg2NyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1',
        'Argos128':'https://www.argos.co.uk/product/8476447?clickSR=slp:term:iphone%2012:3:94:1',
        'CurrysPc128':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-128-gb-black-10215602-pdt.html',
        'CarphoneWarehouse128':'https://www.carphonewarehouse.com/apple/iphone-12.html#!colour=black&capacity=128GB&dealType=sf',
        'Apple128':'https://www.apple.com/uk/shop/buy-iphone/iphone-12',
        'JohnLewis128':'https://www.johnlewis.com/apple-iphone-12-ios-6-1-inch-5g-sim-free-128gb/black/p5178119',
        'GiffGaff128':'https://www.giffgaff.com/mobile-phones/apple/iphone-12-5g/new',

        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-12-dual-sim-black~c12871~p26038731/',
        'CurrysPc256':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-12-256-gb-black-10215608-pdt.html',
        'Amazon256':'https://www.amazon.co.uk/New-Apple-iPhone-12-128GB/dp/B08L5Q3X82/ref=sr_1_1_sspa?dchild=1&keywords=iphone%2B12&qid=1609334864&quartzVehicle=93-1814&replacementKeywords=iphone&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQVVBQUxQWVA2QldWJmVuY3J5cHRlZElkPUEwNTg3MjkyMlhWNE8zVEtWSkQ1UCZlbmNyeXB0ZWRBZElkPUEwMDQxMTE5MjBRWlI5VDE5QVg2NyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1',
        'Argos256':'https://www.argos.co.uk/product/8480093?clickSR=slp:term:iphone%2012:5:18:1',
        'GiffGaff256':'https://www.giffgaff.com/mobile-phones/apple/iphone-12-5g/new',
        'JohnLewis256':'https://www.johnlewis.com/apple-iphone-12-ios-6-1-inch-5g-sim-free-256gb/black/p5178120',
        'CarphoneWarehouse256':'https://www.carphonewarehouse.com/apple/iphone-12.html#!colour=black&capacity=256GB&dealType=sf',
        'Apple256':'https://www.apple.com/uk/shop/buy-iphone/iphone-12',


    }



    def getListPrice_BrandNew(self):
        l = [
            self.getPrice_vendi_64gb(),
            self.getPrice_ebay_64gb(),
            self.getPrice_GiffGaff_64gb(),
            self.getPrice_CarphoneWarehouse_64gb(),
            self.getPrice_Argos_64gb(),
            self.getPrice_JohnLewis_64gb(),
            self.getPrice_Amazon_64gb(),
            self.getPrice_Apple_64gb(),
            self.getPrice_CurrysPc_64gb(),
            self.getPrice_vendi_128gb(),
            self.getPrice_OnBuy_128gb(),
            self.getPrice_ebay_128gb(),
            self.getPrice_Amazon_128gb(),
            self.getPrice_Apple_128gb(),
            self.getPrice_CurrysPc_128gb(),
            self.getPrice_CarphoneWarehouse_128gb(),
            self.getPrice_Apple_128gb(),
            self.getPrice_JohnLewis_128gb(),
            self.getPrice_GiffGaff_128gb(),
            self.getPrice_OnBuy_256gb(),
            self.getPrice_CurrysPc_256gb(),
            self.getPrice_Amazon_256gb(),
            self.getPrice_Argos_256gb(),
            self.getPrice_GiffGaff_256gb(),
            self.getPrice_JohnLewis_256gb(),
            self.getPrice_CarphoneWarehouse_256gb(),
            self.getPrice_Apple_256gb(),
        ]
        return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))

    def getData_BrandNew(self):
        colors = ['White', 'Black', 'Blue', 'Green','Red']
        IPhones = []
        try:
            prices = self.getListPrice_BrandNew()
        except:
            raise ExceptionBreak("Error in Iphone 12")
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone12',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    def getPrice_OnBuy_256gb(self):
        url = self.websites['OnBuy256']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_CurrysPc_256gb(self):
        url = self.websites['CurrysPc256']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_Amazon_256gb(self):
        return self.getPrice_Apple_256gb()

    def getPrice_Argos_256gb(self):
        return self.getPrice_Apple_256gb()

    def getPrice_GiffGaff_256gb(self):
        return self.getPrice_Apple_256gb()

    def getPrice_JohnLewis_256gb(self):
        url = self.websites['JohnLewis256']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')

    def getPrice_CarphoneWarehouse_256gb(self):
        url = self.websites['CarphoneWarehouse256']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-black-256gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-blue-256gb']

    def getPrice_Apple_256gb(self):
        url = self.websites['Apple256']
        return self.get_soap(url).find_all('span', class_='current_price')[25].text


    def getPrice_vendi_128gb(self):
        url = self.websites['vendi128']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text))

    def getPrice_OnBuy_128gb(self):
        url = self.websites['OnBuy128']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_ebay_128gb(self):
        url = self.websites['ebay128']
        return self.get_soap(url).find('div', class_ = 'display-price').text

    def getPrice_Amazon_128gb(self):
        return '£836.17'

    def getPrice_Argos_128gb(self):
        return '£849.00'

    def getPrice_CurrysPc_128gb(self):
        url = self.websites['CurrysPc128']
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_CarphoneWarehouse_128gb(self):
        url = self.websites['CarphoneWarehouse128']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-black-128gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-blue-128gb']

    def getPrice_Apple_128gb(self):
        url = self.websites['Apple128']
        return self.get_soap(url).find_all('span', class_='current_price')[20].text

    def getPrice_JohnLewis_128gb(self):
        url = self.websites['JohnLewis128']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')


    def getPrice_GiffGaff_128gb(self):
        return self.getPrice_Apple_128gb()


    def getPrice_vendi_64gb(self):
        url = self.websites['vendi64']
        try:
            return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text))
        except:
            return self.getPrice_Apple_64gb()

    def getPrice_ebay_64gb(self):
        url = self.websites['ebay64']
        return self.get_soap(url).find('span', id = 'prcIsum').text.split()[0]

    def getPrice_GiffGaff_64gb(self):
        return self.getPrice_Apple_64gb()

    def getPrice_CarphoneWarehouse_64gb(self):
        url = self.websites['CarphoneWarehouse64']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-black-64gb']
        except:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-blue-64gb']

    def getPrice_Argos_64gb(self):
        url = self.websites['Argos64']
        return self.getPrice_Apple_64gb()

    def getPrice_JohnLewis_64gb(self):
        url = self.websites['JohnLewis64']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')

    def getPrice_Amazon_64gb(self):
        return self.getPrice_Apple_64gb()

    def getPrice_Apple_64gb(self):
        url = self.websites['Apple64']
        return self.get_soap(url).find_all('span', class_='current_price')[0].text

    def getPrice_CurrysPc_64gb(self):
        url = self.websites['CurrysPc64']
        return self.get_soap(url).find('strong', class_='current').text
































