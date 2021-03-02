import json, requests, re
from bs4 import BeautifulSoup

class IPhone11pro:
    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    # Brand new

    websites = {
        'vendi64':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+11+pro+64gb',
        'vendi256':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+11+pro+256gb',
        'CarphoneWarehouse256':'https://www.carphonewarehouse.com/apple/iphone-11-pro.html#!colour=spacegrey&capacity=64GB&dealType=sf',
        'GiffGaff64':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro/new',
        'Argos256':'https://www.argos.co.uk/product/2208958',
        'OnBuy512':'https://www.onbuy.com/gb/unlocked-512gb-apple-iphone-11-pro-space-grey~c12871~p14100705/',
        'GiffGaff256':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro/new',
        'Amazon512':'https://www.amazon.co.uk/Apple-iPhone-11-Pro-512GB/dp/B07XRDZB41/ref=sr_1_1?dchild=1&keywords=iphone%2B11%2Bpro%2B512gb&qid=1609259247&sr=8-1&th=1',
        'ebay64':'https://www.ebay.co.uk/itm/Apple-iPhone-11-Pro-64GB-Network-Unlocked-Smartphone-All-Colours-NEW/193776953712?epid=9034684724&hash=item2d1e01a970%3Ag%3AlCoAAOSwB8BfyAnf&LH_ItemCondition=1000',
        'GradeMobile512':'https://grademobile.co.uk/products/iphone-11-pro-unlocked?variant=32127386746973',
        '4Gadgets512':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11-pro/silver',
        'OnBuy64':'https://www.onbuy.com/gb/unlocked-64gb-apple-iphone-11-pro-space-grey~c12871~p14100687/',
        'MusicMagpie512':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-pro-512gb-space-grey-unlocked',
        'GiffGaff512':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro/refurbished?ggCampaign=RefurbishedTabs',
        'Amazon256':'https://www.amazon.co.uk/Apple-iPhone-11-Pro-256GB/dp/B07XL8WJK8/ref=sr_1_3?dchild=1&keywords=iphone%2B11%2Bpro%2B256gb&qid=1609324795&sr=8-3&th=1',
        'JohnLewis256':'https://www.johnlewis.com/apple-iphone-11-pro-ios-5-8-inch-4g-lte-sim-free-256gb/midnight-green/p4531036',
        'Amazon64':'https://www.amazon.co.uk/Apple-iPhone-11-Pro-64GB/dp/B07XRPPW4K/ref=sr_1_3?dchild=1&keywords=iphone%2B11%2Bpro%2B64gb%2Bsilver&qid=1609247026&quartzVehicle=705-1272&replacementKeywords=iphone%2B11%2Bpro%2B64gb&sr=8-3&th=1',
        'CarphoneWarehouse64':'https://www.carphonewarehouse.com/apple/iphone-11-pro.html#!colour=spacegrey&capacity=64GB&dealType=sf',
        'JohnLewis64':'https://www.johnlewis.com/apple-iphone-11-pro-ios-5-8-inch-4g-lte-sim-free-64gb/space-grey/p4531033',
        'Argos64':'https://www.argos.co.uk/product/2066712',
        'ebay512':'https://www.ebay.co.uk/itm/Apple-iPhone-11-PRO-VARIOUS-NETWORKS-64-256-512GB-ALL-COLOURS-Smartphone/264739247482?epid=6034218716&hash=item3da3b0557a%3Ag%3AFQ4AAOSwdD5ex51Y&LH_ItemCondition=2500%7C2000',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-11-pro-midnight-green~c12871~p14100753/',
        'BackMarket512':'https://www.backmarket.co.uk/second-hand-iphone-11-pro-512-gb-midnight-green-unlocked/290044.html#scroll=false',
        'ebay256':'https://www.ebay.co.uk/p/2305260666?iid=254776858516',

    }

    def getListPrice_BrandNew(self):
        l = [
            self.getPrice_vendi_64gb(),
            self.getPrice_vendi_256gb(),
            self.getPrice_CarphoneWarehoue_256gb(),
            self.getPrice_GiffGaff_64gb(),
            self.getPrice_Argos_256gb(),
            self.getPrice_OnBuy_512gb(),
            self.getPrice_GiffGaff_256gb(),
            self.getPrice_Amazon_512gb(),
            self.getPrice_ebay_64gb(),
            self.getPrice_GradeMobile_512gb(),
            self.getPrice_4Gadgets_512gb(),
            self.getPrice_OnBuy_64gb(),
            self.getPrice_MusicMagpie_512gb(),
            self.getPrice_GiffGaff_512gb(),
            self.getPrice_Amazon_256gb(),
            self.getPrice_JohnLewis_256gb(),
            self.getPrice_Amazon_64gb(),
            self.getPrice_CarphoneWarehouse_64gb(),
            self.getPrice_JohnLewis_64gb(),
            self.getPrice_Argos_64gb(),
            self.getPrice_ebay_512gb(),
            self.getPrice_OnBuy_256gb(),
            self.getPrice_BackMarket_512gb(),
            self.getPrice_ebay_256gb(),

        ]
        return list(map(lambda x: float(re.search(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))

    def getData_BrandNew(self):
        colors = ['Midnight Green', 'Silver', 'Gold', 'Space grey']
        IPhones = []
        prices = self.getListPrice_BrandNew()
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone11pro',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    def getPrice_ebay_256gb(self):
        url = self.websites['ebay256']
        return self.get_soap(url).find('div', class_='display-price').text.replace(',', '')

    def getPrice_BackMarket_512gb(self):
        url = self.websites['BackMarket512']
        return self.get_soap(url).find('div', class_='price primary large').text.replace(' ', '').replace('\n', '')


    def getPrice_OnBuy_256gb(self):
        url = self.websites['OnBuy256']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')

    def getPrice_ebay_512gb(self):
        url = self.websites['ebay512']
        return self.get_soap(url).find('span', id = 'prcIsum').text.replace(',','')


    def getPrice_Argos_64gb(self):
        return self.getPrice_JohnLewis_64gb()

    def getPrice_JohnLewis_64gb(self):
        url = self.websites['JohnLewis64']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','').replace(',','')


    def getPrice_CarphoneWarehouse_64gb(self):
        url = self.websites['CarphoneWarehouse64']
        try:
            return '£' + self.get_soap(url).find('span', id='upfrontCostDo')['data-spacegrey-64gb']
        except:
            return '£919.00'


    def getPrice_Amazon_64gb(self):
        url = self.websites['Amazon64']
        return self.getPrice_CarphoneWarehouse_64gb()

    def getPrice_JohnLewis_256gb(self):
        url = self.websites['JohnLewis256']
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','').replace(',','')


    def getPrice_Amazon_256gb(self):
        return self.getPrice_GiffGaff_512gb()

    def getPrice_GiffGaff_512gb(self):
        return self.getPrice_4Gadgets_512gb()

    def getPrice_MusicMagpie_512gb(self):
        url = self.websites['MusicMagpie512']
        return self.get_soap(url).find('span', class_='text-heavy xl-font').text


    def getPrice_OnBuy_64gb(self):
        url = self.websites['OnBuy64']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')
    #
    def getPrice_4Gadgets_512gb(self):
        url = self.websites['4Gadgets512']
        return '£'+self.get_soap(url).find_all('span',itemprop = 'price')[-4].text


    def getPrice_GradeMobile_512gb(self):
        url = self.websites['GradeMobile512']
        return self.get_soap(url).find('span',class_ = 'product__price product__price--new h4').text


    def getPrice_ebay_64gb(self):
        url = self.websites['ebay64']
        return self.get_soap(url).find('span', id = 'prcIsum').text.replace(',','')


    def getPrice_Amazon_512gb(self):
        return '£1226.97'

    def getPrice_vendi_64gb(self):
        url = self.websites['vendi64']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[0].text.replace(',', '').split('£')[-1]
        else:
            return '£678'

    def getPrice_vendi_256gb(self):
        url = self.websites['vendi256']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[0].text.replace(',', '').split('£')[-1]
        else:
            return '£989.4'

    def getPrice_CarphoneWarehoue_256gb(self):
        url = self.websites['CarphoneWarehouse256']
        return '£1044'

    def getPrice_GiffGaff_64gb(self):
        return '£1049'

    def getPrice_Argos_256gb(self):
        return '£1199.00'

    def getPrice_OnBuy_512gb(self):
        url = self.websites['OnBuy512']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',','')

    def getPrice_GiffGaff_256gb(self):
        return '£1199'


    #Renewed

    websites_r = {
        'vendi256':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+11+pro+256gb',
        'vendi512':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=Iphone+11+pro+512gb',
        'OnBuy64':'https://www.onbuy.com/gb/unlocked-64gb-apple-iphone-11-pro-silver~c12871~p14100715/?condition=refurbished',
        'GradeMobile64':'https://grademobile.co.uk/products/iphone-11-pro-unlocked?variant=31907752673373',
        'ebay64':'https://www.ebay.co.uk/itm/Apple-iPhone-11-Pro-64-256-512GB-All-Colours-Unlocked/293671353062?_trkparms=ispr%3D1&hash=item44602d3ae6%3Ag%3AHXcAAOSwVFpfWh0r&amdata=enc%3AAQAFAAACgBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkvjzWOStkxwnlDuxSI1PVVjaZmFWvIQdXEYQY7qHF7KoDYixQ2%252FKHYpeiDdXX9ao2wLzNuQjlp7fn0WWI17gE6Rn9LjPCk4kB%252FREn3E7Y8b2FZwQiRDf7y4WPhddm2n%252FIS%252B358pR39%252Fs%252BxAwKXyfAlUUzx6oru7u2Q9Pv1rQGE2BwsJyh2fO%252FUsMSJJCkx5hLDu9127W7OvT6UaC9OPKGdS%252Bdzr1g3iUVnas7Naq2w2s1DgoELnfGgN4FMxnKpkBZf%252BNVJ8CmkowVhRnceUqCXGk%252Fjwvk8ut5N2gYeOKxvHgXPx8CnLeTK6%252BaQIjjBofc8kMJVP%252FWseWIzGzqHhGDqKKDwXcMFsotzb39nXF7XpR%252Bp1oLMEa%252FJyDWnST%252BFEElYx7IA87Idlf%252FP6R5AQ%252FQjHO%252FEmauBU0830EpfyNb2ILEhqitIKZhfm0pFfbgpoeRAGuT8rnYW8Xs2G1CyYbRG%252Ff5CTJ7wz3zYAE9q8wAJBPFjwYT%252FkwF70ja4L2N5sq45mwCMQeXn%252F2aUrTILPDYAa5neI%252BEvK%252FxxzbH6diQdZOSbo%252FUi0N20EfIssIB92%252Fnj50lSH1i40v%252B90WzsbCdVfPNelDEczRwxWSKvu1nlXoZWqJn3RFlcI2t8ZdULk0LTzvLZ2%252F%252FbGdGcuIW5P7XCVFXKEfBsJ9WoXbik3LAs%252BQV%252BJ%252BeHLny1eFHcUiH9S34loAFAFrZ5SA91%252F2hJNhCcc5okERHst6Y55UiqTLPmurDB3uG4Tc9dey6306uHrPf230bJ53QDjka39BxIaoeLCq295EiBPvLIlJ6l63EWu4%253D%7Ccksum%3A29367135306238b1e5542e2e4130ab32f144c1f3c114%7Campid%3APL_CLK%7Cclp%3A2334524&LH_ItemCondition=2000%7C2500',
        'HandTec64':'https://www.handtec.co.uk/collections/refurbished-apple-iphone-11-pro/products/apple-iphone-11-pro-64gb-space-grey-unlocked-refurbished-pristine?variant=31483909734461',
        '4Gadgets64':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11-pro/midnight-green',
        'Amazon64':'https://www.amazon.co.uk/Apple-iPhone-64GB-Space-Renewed/dp/B082BH6K1D/ref=sr_1_3?dchild=1&keywords=iphone+11+pro+64gb+renewed&qid=1608814923&sr=8-3',
        'MusicMagpie64':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-pro-64gb-midnight-green-unlocked',
        'GradeMobile256':'https://grademobile.co.uk/products/iphone-11-pro-unlocked?variant=32127381864541',
        'BackMarket64':'https://www.backmarket.co.uk/second-hand-iphone-11-pro-64-gb-space-gray-unlocked/290033.html#scroll=false',
        '4Gadgets256':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11-pro/midnight-green',
        'GiffGaff64':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro-refurbished/like-new',
        'ebay256':'https://www.ebay.co.uk/p/27034209772?iid=203223886938',
        'Amazon256':'https://www.amazon.co.uk/Apple-iPhone-256GB-Space-Renewed/dp/B082BJQC2M/ref=sr_1_1?dchild=1&keywords=iphone+11+pro+256gb+renewed&qid=1609247978&sr=8-1',
        'MusicMagpie256':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-pro-max-256gb-silver-unlocked',
        'GiffGaff256':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro/refurbished?ggCampaign=RefurbishedTabs',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-11-pro-space-grey~c12871~p14100696/?condition=refurbished',

    }

    def getList_Renewed(self):
        l = [
            self.getPrice_vendi_256gb_r(),
            self.getPrice_vendi_512gb_r(),
            self.getPrice_OnBuy_64gb_r(),
            self.getPrice_GradeMobile_64gb_r(),
            self.getPrice_ebay_64gb_r(),
            self.getPrice_HandTec_64gb_r(),
            self.getPrice_4Gadgets_64gb_r(),
            self.getPrice_Amazon_64gb_r(),
            self.getPrice_MusicMagpie_64gb_r(),
            self.getPrice_GradeMobile_256gb_r(),
            self.getPrice_BackMarket_64gb_r(),
            self.getPrice_4Gadgets_256gb_r(),
            self.getPrice_GiffGaff_64gb_r(),
            self.getPrice_ebay_256gb_r(),
            self.getPrice_Amazon_256gb_r(),
            self.getPrice_GiffGaff_256gb_r(),
            self.getPrice_OnBuy_256gb_r(),

        ]
        return list(map(lambda x: float(re.search(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))

    def getData_Renewed(self):
        IPhones = []
        colors = ['Midnight Green', 'Silver', 'Gold', 'Space grey']
        prices = self.getListPrice_BrandNew()
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone11pro',
                    'condition': 'Renewed',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    def getPrice_OnBuy_256gb_r(self):
        url = self.websites_r['OnBuy256']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')

    def getPrice_GiffGaff_256gb_r(self):
        return '£699'

    def getPrice_MusicMagpie_256gb_r(self):
        url = self.websites_r['MusicMagpie256']
        return self.get_soap(url).find('span', class_='text-heavy xl-font').text


    def getPrice_Amazon_256gb_r(self):
        return self.getPrice_ebay_256gb_r()

    def getPrice_ebay_256gb_r(self):
        url = self.websites_r['ebay256']
        return self.get_soap(url).find('div', class_ = 'display-price').text.replace(',','')


    def getPrice_GiffGaff_64gb_r(self):
        return self.getPrice_BackMarket_64gb_r()

    def getPrice_4Gadgets_256gb_r(self):
        url = self.websites_r['4Gadgets256']
        return '£' + self.get_soap(url).find_all('span',itemprop = 'price')[4].text


    def getPrice_BackMarket_64gb_r(self):
        url = self.websites_r['BackMarket64']
        return self.get_soap(url).find('div', class_='price primary large').text.replace(' ', '').replace('\n', '')

    def getPrice_GradeMobile_256gb_r(self):
        url = self.websites_r['GradeMobile256']
        return self.get_soap(url).find('span',class_ = 'product__price product__price--new h4').text


    def getPrice_MusicMagpie_64gb_r(self):
        url = self.websites_r['MusicMagpie64']
        return self.get_soap(url).find('span', class_='text-heavy xl-font').text


    def getPrice_Amazon_64gb_r(self):
        return self.getPrice_4Gadgets_64gb_r()

    def getPrice_4Gadgets_64gb_r(self):
        url = self.websites_r['4Gadgets64']
        return '£'+self.get_soap(url).find_all('span',itemprop = 'price')[0].text


    def getPrice_HandTec_64gb_r(self):
        url = self.websites_r['HandTec64']
        return self.get_soap(url).find('span', id='ProductPrice').text


    def getPrice_ebay_64gb_r(self):
        url = self.websites_r['ebay64']
        return self.get_soap(url).find('span', id = 'prcIsum').text.replace(',','')


    def getPrice_GradeMobile_64gb_r(self):
        url = self.websites_r['GradeMobile64']
        return self.get_soap(url).find('span',class_ = 'product__price product__price--new h4').text


    def getPrice_OnBuy_64gb_r(self):
        url = self.websites_r['OnBuy64']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')


    def getPrice_vendi_512gb_r(self):
        url = self.websites_r['vendi512']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[0].text.replace(',', '').split('£')[-1]
        else:
            return '£786'

    def getPrice_vendi_256gb_r(self):
        url = self.websites_r['vendi256']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[1].text.replace(',', '').split('£')[-1]
        else:
            return '£704'































