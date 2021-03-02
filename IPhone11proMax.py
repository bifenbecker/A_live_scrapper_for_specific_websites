import json, requests, re
from bs4 import BeautifulSoup

class IPhone11proMax:
    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    # Brand new

    websites = {
        'Amazon256':'https://www.amazon.co.uk/Apple-iPhone-256GB-Silver-Renewed/dp/B082BH14PK/ref=sr_1_1?dchild=1&keywords=iphone%2B11%2Bpro%2Bmax%2B256gb%2Brenewed&qid=1609330154&sr=8-1&th=1',
        'MusicMagpie256':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-pro-max-256gb-silver-unlocked',
        'ebay64':'https://www.ebay.co.uk/itm/NEW-Apple-iPhone-11-Pro-Max-64GB-Space-Grey-Unlocked-A2218-APPLE-WARRANTY/254544401593?epid=14034212889&hash=item3b440754b9%3Ag%3AUjkAAOSwyp5ecj8b&LH_ItemCondition=1000',
        'vendi64':'https://shop.vendiapp.com/products/apple-iphone-11-pro-max-64gb-21?_pos=1&_sid=71c75c1d0&_ss=r',
        'OnBuy64':'https://www.onbuy.com/gb/unlocked-64gb-apple-iphone-11-pro-max-silver~c12871~p14100378/',
        'CarphoneWarehouse64':'https://www.carphonewarehouse.com/apple/iphone-11-pro-max.html#!colour=spacegrey&capacity=64GB&dealType=sf',
        'vendi256':'https://shop.vendiapp.com/products/apple-iphone-11-pro-max-256gb-18?_pos=2&_sid=73f5d35e9&_ss=r',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-11-pro-max-gold~c12871~p14100565/',
        'ebay256':'https://www.ebay.co.uk/p/27034209624?iid=264923792409',
        'Amazon64':'https://www.amazon.co.uk/Apple-iPhone-Pro-Max-64GB/dp/B07XRP1G1D/ref=sr_1_1?dchild=1&keywords=iphone+11+pro+max+64gb&qid=1609329338&refinements=p_n_condition-type%3A12319067031&rnid=12319066031&sr=8-1',
        'GiffGaff64':'https://www.giffgaff.com/internal-error',
        'CarphoneWarehouse256':'https://www.carphonewarehouse.com/apple/iphone-11-pro-max.html#!colour=spacegrey&capacity=256GB&dealType=sf',
        'Argos64':'https://www.argos.co.uk/search/iphone-11-pro-max-64gb/?clickOrigin=searchbar:productdetailsterm:iphone+11+pro+max+64gb',
        'vendi512':'https://shop.vendiapp.com/products/apple-iphone-11-pro-max-512gb?_pos=3&_sid=5ef24a87d&_ss=r',
        'OnBuy512':'https://www.onbuy.com/gb/unlocked-512gb-apple-iphone-11-pro-max-silver~c12871~p14100396/',
        'Argos256':'https://www.argos.co.uk/search/iphone-11-pro-max-256gb/?clickOrigin=searchbar:productdetailsterm:iphone+11+pro+max+256gb',
        'GiffGaff256':'https://www.giffgaff.com/internal-error',
        'CarphoneWarehouse512':'https://www.carphonewarehouse.com/apple/iphone-11-pro-max.html#!colour=spacegrey&capacity=512GB&dealType=sf',
        'Argos512':'https://www.argos.co.uk/search/iphone-11-pro-max-512gb/?clickOrigin=searchbar:productdetailsterm:iphone+11+pro+max+512gb',
        'GiffGaff512':'https://www.giffgaff.com/internal-error',
    }

    def getListPrice_BrandNew(self):
        l = [
            self.getPrice_Amazon_256gb(),
            self.getPrice_MusicMagpie_256gb(),
            self.getPrice_ebay_64gb(),
            self.getPrice_vendi_64gb(),
            self.getPrice_OnBuy_64gb(),
            self.getPrice_CarphoneWarehouse_64gb(),
            self.getPrice_vendi_256gb(),
            self.getPrice_OnBuy_256gb(),
            self.getPrice_ebay_256gb(),
            self.getPrice_Amazon_64gb(),
            self.getPrice_GiffGaff_64gb(),
            self.getPrice_CarphoneWarehouse_256gb(),
            self.getPrice_Argos_64gb(),
            self.getPrice_vendi_512gb(),
            self.getPrice_OnBuy_512gb(),
            self.getPrice_Argos_256gb(),
            self.getPrice_GiffGaff_256gb(),
            self.getPrice_CarphoneWarehouse_512gb(),
            self.getPrice_Argos_512gb(),
            self.getPrice_GiffGaff_512gb(),

        ]
        return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))


    def getData_BrandNew(self):
        colors = ['Gold', 'Green', 'Silver', 'Space gray']
        IPhones = []
        prices = self.getListPrice_BrandNew()
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone11proMax',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    def getPrice_Amazon_256gb(self):
        return '£801.94'

    def getPrice_MusicMagpie_256gb(self):
        url = self.websites['MusicMagpie256']
        return self.get_soap(url).find('span', class_ = 'text-heavy xl-font').text

    def getPrice_ebay_64gb(self):
        url = self.websites['ebay64']
        return self.get_soap(url).find('span', id = 'prcIsum').text

    def getPrice_vendi_64gb(self):
        url = self.websites['vendi64']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text))

    def getPrice_OnBuy_64gb(self):
        url = self.websites['OnBuy64']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getPrice_CarphoneWarehouse_64gb(self):
        return '£999'

    def getPrice_vendi_256gb(self):
        url = self.websites['vendi256']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text))

    def getPrice_OnBuy_256gb(self):
        url = self.websites['OnBuy256']
        try:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',','')
        except:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',',
                                                                                                                  '')

    def getPrice_ebay_256gb(self):
        url = self.websites['ebay256']
        return self.get_soap(url).find('div', class_ = 'display-price').text.replace(',','')

    def getPrice_Amazon_64gb(self):
        return '£1149'

    def getPrice_GiffGaff_64gb(self):
        return '£1149'

    def getPrice_CarphoneWarehouse_256gb(self):
        return '£1149'

    def getPrice_Argos_64gb(self):
        url = self.websites['Argos64']
        return '£1049.00'

    def getPrice_vendi_512gb(self):
        url = self.websites['vendi512']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text)).replace(',','')

    def getPrice_OnBuy_512gb(self):
        url = self.websites['OnBuy512']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',','')

    def getPrice_Argos_256gb(self):
        return '£1199.00'

    def getPrice_GiffGaff_256gb(self):
        return '£1299'

    def getPrice_CarphoneWarehouse_512gb(self):
        return '£1349'

    def getPrice_Argos_512gb(self):
        return '£1399.00'

    def getPrice_GiffGaff_512gb(self):
        return '£1499'

    #Renewed

    websites_r = {
        '4Gadgets64':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11-pro/midnight-green',
        'Amazon64':'https://www.amazon.co.uk/Apple-iPhone-Midnight-Green-Renewed/dp/B082BGTZGC/ref=sr_1_1?dchild=1&keywords=iphone%2B11%2Bpro%2Bmax&qid=1609325807&refinements=p_n_condition-type%3A13736824031&sr=8-1&th=1',
        'ebay64':'https://www.ebay.co.uk/itm/Apple-iPhone-11-Pro-Max-64-256-512GB-All-Colours-Unlocked/293671354412?hash=item44602d402c%3Ag%3AJoMAAOSwq4tfWh0u&LH_ItemCondition=2000%7C2500',
        'vendi64':'https://shop.vendiapp.com/products/apple-iphone-11-pro-max-64gb-19?_pos=3&_sid=f9df52708&_ss=r',
        '4Gadgets256':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11-pro/midnight-green',
        'vendi256':'https://shop.vendiapp.com/products/apple-iphone-11-pro-max-3?_pos=1&_sid=08a0dbb6b&_ss=r',
        'OnBuy256':'https://www.onbuy.com/gb/unlocked-256gb-apple-iphone-11-pro-max-space-grey~c12871~p14100443/?condition=refurbished',
        'ebay256':'https://www.ebay.co.uk/itm/Apple-iPhone-11-Pro-Max-64GB-256GB-512GB-ALL-COLOURS-UNLOCKED-VARIOUS-GRADES/333724832936?epid=11034210143&_trkparms=ispr%3D1&hash=item4db38cd4a8:g:S0kAAOSwsypeqUqs&amdata=enc%3AAQAFAAACgBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkCrLl8erj3ATP5raQxjc%252F%252B6hd1s%252B%252BLxLmA%252F5LUzmex6DAwnFHnSTPiBJJiTsd3arahGCpdKwyQRuiF%252FWEPXhaBZ6GuDVHZngWjOYDdUCi%252BcAXF8krle4IZkTfotI8KnzZt93tr0xEPQ8q3k5q6ZbyeBOQxKjspeRL39ZQ21VmnrW9bzO33%252BIy%252B0SjmTNNLTsUD5jJ3q18fqDQu6Zp%252B3CSKuYYuQpsXRPKvMGuyfcxB7xAhe8jZFoYO8A383Gbc5026buArnhOb1MMRIxUkIxu8bOLiV6I%252BSyAgoiKf7oEX6GRfqhTRQYDpKvUt0z2BSwsW9tutMXfWuCG0K%252BnwnPpmBEPuvadLJHovwGJxDuiu9ARCJhOpG1am6fptis70ReDTFCYwPryP8aeevFIHiIlOUUClpFBRhntn9Tt476MVHHleCPb149jiKv5PkzFG9G7l0WlZ5bFHVsbplLmSNW9MkXxxIspSZXTADEA%252FGvBAsw0O6PxfuPR86W%252FDAWtUV0YStYiL2I3AR8SRipuyQ2GDaKYbZWbefF3LteYkSjpnLu7xjdYF6dUVDuamxverquBt73I3Ca6536Yx8y1dMaZSZgAoc92OoRHQU8YOvUr9H%252BxDxNhc73Eozp7G4drN7tu9t3VgEJNG5jZO%252FQeU12B80AtQB8ny32JViakGZeLFT4T5kq6%252FyoNyWrF%252FHZbnk0eiPqEuY5ciqsgoArd83u5jkTCzZJuZLxSKZkZdlDFUkpch5O3Dw36yVBH0MYV4OAPsju61VP%252Bj75Te%252BUVT3MgvnW2W3bgExs%252B12YezTO%252FGLI%253D%7Ccksum%3A333724832936c158c595d7d048a3a9310173fb9b5522%7Campid%3APL_CLK%7Cclp%3A2334524',
        '4Gadgets512':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11-pro/midnight-green',
        'GradeMobile256':'https://grademobile.co.uk/products/iphone-11-pro-max-unlocked?variant=32127411945565',
        'GradeMobile64':'https://grademobile.co.uk/products/iphone-11-pro-max-unlocked?variant=31912487026781',
        'vendi512':'https://shop.vendiapp.com/products/apple-iphone-11-pro-max-512gb-1?_pos=2&_sid=f673375fd&_ss=r',
        'Amazon512':'https://www.amazon.co.uk/Apple-iPhone-512GB-Midnight-Renewed/dp/B082BH1T8T/ref=sr_1_2?dchild=1&keywords=apple+iphone+11promax+512gb+%28renewed%29&qid=1609330245&sr=8-2',
        'GradeMobile512':'https://grademobile.co.uk/products/iphone-11-pro-max-unlocked?variant=32127422496861',
        'BackMarket64':'https://www.backmarket.co.uk/second-hand-iphone-11-pro-max-64-gb-midnight-green-unlocked/290048.html#?l=0',
        'MusicMagpie512':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-pro-max-512gb-space-grey-unlocked-c889ad69-7cbb-47fe-87a6-395b1ee086b1',
        'BackMarket256':'https://www.backmarket.co.uk/second-hand-iphone-11-pro-max-256-gb-midnight-green-unlocked/290052.html#?l=0',
        'ebay512':'https://www.ebay.co.uk/itm/Apple-iPhone-11-Pro-Max-64GB-256GB-512GB-Unlocked-Smartphone-Various-Colours/383223775930?epid=6034218752&_trkparms=ispr%3D1&hash=item5939eac2ba%3Ag%3A6QAAAOSwzZFeJZ5c&amdata=enc%3AAQAFAAACgBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkxFtV7J5P58ubuVigtBH%252Fe7NK7rv3N8eNS2k3fXDzs0RGW6S73tP2ZUIanYjXhjJxHeKbj%252BecQdD%252B3fWFbUOqX84Yrn4nQ9d6r3fu5zAUBMiGcxyJX6E5Kpf0xO5CTw5%252BKm4TpB0t7CDEwGtQWf3dvuAnPuE1xeNRpcaq%252BzsJzozwerfWyn79DXuPHxCRub1f4VQW1qkHS3CUnV%252BWlHJtlnWdxSNpIoyKS%252BCuZnvdyapPMb1r207EJQqNY5zK%252Fd%252B0eDy%252Beots5WHdbPGV4E28VO4g6LMGrkx83UaiyjAnvPzvP1d5D2zlzdqsCE4AUDEdCNc5ILdaume6zJN7ITr7RmPg7qhj4IMFQ4%252B3cCH8MLznik0WK7HfsPMhlZr1WIyPQlcNOhqjTXhLZRCucPOZFhEnpwQk%252FBOr1fKCMLPDPaMRcMvDbwaSB65jwinmaWTAzIGT8qTR%252BMlMQ8PUIzvBXHl2x%252BdY1OgLi8Blll3wopI68SzABgx5UPwdmbysq8oB5waDv8KvIkKjTpB2i7WZRQlE0hlgT1to%252BYmkE1fq62tBtygCrbZ7tn3R1DAwEJVLLVC%252FftIGtVMfJnpheGVg8adbYf3O4%252B2avuRmvrU5ZOlveyy96mHW2rGcImtP8pkD05nNPLmAMIzfgockfQcHN1u%252FXi4GTldITDpWy682QkVvUe3U9lQHbKGmHHKrz75cS4KmdDcCOor0v3W4J1iJoW03Hd91uDD9QSUsqSc2crTUvMu2uZKGOz7Xj%252F3DSCXbzbtzT68zivkIP4BM5bgpajQOjyyORFsxULhAyuRHZS8%253D%7Ccksum%3A383223775930a7408bee071d4660b678026e2f1f0f1b%7Campid%3APL_CLK%7Cclp%3A2334524&LH_ItemCondition=2000%7C2500',
        'GiffGaff64':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro-max-refurbished/like-new',
        'GiffGaff256':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro-max-refurbished/like-new',
        'GiffGaff512':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11-pro-max-refurbished/like-new',

    }

    def getListPrice_Renewed(self):
        l = [
            self.getPrice_4Gadgets_64gb_r(),
            self.getPrice_Amazon_64gb_r(),
            self.getPrice_ebay_64gb_r(),
            self.getPrice_vendi_64gb_r(),
            self.getPrice_4Gadgets_256gb_r(),
            self.getPrice_vendi_256gb_r(),
            self.getPrice_OnBuy_256gb_r(),
            self.getPrice_ebay_256gb_r(),
            self.getPrice_4Gadgets_512gb_r(),
            self.getPrice_GradeMobile_256gb_r(),
            self.getPrice_GradeMobile_64gb_r(),
            self.getPrice_vendi_512gb_r(),
            self.getPrice_Amazon_512gb_r(),
            self.getPrice_GradeMobile_512gb_r(),
            self.getPrice_BackMarket_64gb_r(),
            self.getPrice_MusicMagpie_512gb_r(),
            self.getPrice_BackMarket_256gb_r(),
            self.getPrice_ebay_512gb_r(),
            self.getPrice_GiffGaff_64gb_r(),
            self.getPrice_GiffGaff_256gb_r(),
            self.getPrice_GiffGaff_512gb_r(),
        ]
        return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',x)[0]), l))

    def getData_Renewed(self):
        colors = ['Gold', 'Green', 'Silver', 'Space gray']
        IPhones = []
        prices = self.getListPrice_BrandNew()
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone11proMax',
                    'condition': 'Renewed',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]',list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    def getPrice_4Gadgets_64gb_r(self):
        url = self.websites_r['4Gadgets64']
        return '£'+self.get_soap(url).find_all('span',itemprop = 'price')[3].text

    def getPrice_Amazon_64gb_r(self):
        return '£699.29'

    def getPrice_ebay_64gb_r(self):
        url = self.websites_r['ebay64']
        return self.get_soap(url).find('span', id='prcIsum').text

    def getPrice_vendi_64gb_r(self):
        url = self.websites_r['vendi64']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text)).replace(',','')

    def getPrice_4Gadgets_256gb_r(self):
        url = self.websites_r['4Gadgets256']
        return '£'+self.get_soap(url).find_all('span',itemprop = 'price')[3].text

    def getPrice_vendi_256gb_r(self):
        url = self.websites_r['vendi256']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text)).replace(',','')

    def getPrice_OnBuy_256gb_r(self):
        url = self.websites_r['OnBuy256']
        try:
            return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '').replace(',','')
        except:
            return self.get_soap(url).find('div', class_='oos-price').text.replace(' ', '').replace('\n', '').replace(',','')


    def getPrice_ebay_256gb_r(self):
        url = self.websites_r['ebay256']
        return '£749.99'

    def getPrice_4Gadgets_512gb_r(self):
        url = self.websites_r['4Gadgets512']
        return '£'+self.get_soap(url).find_all('span',itemprop = 'price')[-4].text

    def getPrice_GradeMobile_256gb_r(self):
        url = self.websites_r['GradeMobile256']
        return self.get_soap(url).find('span',class_ = 'product__price product__price--new h4').text

    def getPrice_GradeMobile_64gb_r(self):
        url = self.websites_r['GradeMobile64']
        return self.get_soap(url).find('span',class_ = 'product__price product__price--new h4').text

    def getPrice_vendi_512gb_r(self):
        url = self.websites_r['vendi512']
        return ''.join(re.findall('\d*|,|.\d', self.get_soap(url).find('span', class_='price').text)).replace(',','')

    def getPrice_Amazon_512gb_r(self):
        return '£839.95'

    def getPrice_GradeMobile_512gb_r(self):
        url = self.websites_r['GradeMobile512']
        return self.get_soap(url).find('span',class_ = 'product__price product__price--new h4').text

    def getPrice_BackMarket_64gb_r(self):
        url = self.websites_r['BackMarket64']
        return self.get_soap(url).find('div', class_='price primary large').text.replace(' ', '').replace('\n', '')

    def getPrice_MusicMagpie_512gb_r(self):
        url =self.websites_r['MusicMagpie512']
        return self.get_soap(url).find('span', class_='text-heavy xl-font').text

    def getPrice_BackMarket_256gb_r(self):
        url = self.websites_r['BackMarket256']
        return self.get_soap(url).find('div', class_='price primary large').text.replace(' ', '').replace('\n', '')

    def getPrice_ebay_512gb_r(self):
        url = self.websites_r['ebay512']
        return '£819.99'

    def getPrice_GiffGaff_64gb_r(self):
        return '£949'

    def getPrice_GiffGaff_256gb_r(self):
        return '£999'

    def getPrice_GiffGaff_512gb_r(self):
        return '£1049'







