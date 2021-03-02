import json, requests, re
from bs4 import BeautifulSoup

class IPhone11:

    #Brand New
    types = ['ebay64','Apple64','GiffGaff64','JohnLewis64','Currys64','Argos64','Amazon64','OnBuy64','Amazon128','GiffGaff128','Currys128','Apple128','JohnLewis128','Argos128','OnBuy128','ebay128']

    websites = {
        'vendi64':'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+11+64gb',
        'ebay64':'https://www.ebay.co.uk/itm/NEW-Apple-MWLT2B-A-iPhone-11-6-1-4G-Smartphone-64GB-Unlocked-Sim-Free-Black/352909507761?epid=22034217345&hash=item522b0bbcb1%3Ag%3Aq4UAAOSwE91d%7ELnh&LH_ItemCondition=1000',
        'Apple64':'https://www.apple.com/uk/shop/buy-iphone/iphone-11',
        'GiffGaff64':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11/new',
        'JohnLewis64':'https://www.johnlewis.com/apple-iphone-11-ios-6-1-inch-4g-lte-sim-free-64gb/green/p4519032',
        'Currys64':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-11-64-gb-black-10197974-pdt.html',
        'Argos64':'https://www.argos.co.uk/product/2153591?clickSR=slp:term:iphone%2011%2064gb:1:125:1',
        'Amazon64':'https://www.amazon.co.uk/Apple-iPhone-11-64GB-Black/dp/B08L6YSCDF/ref=pd_rhf_se_p_img_1?_encoding=UTF8&psc=1&refRID=Q09XWDT1CJTVT1ERRSY9',
        'OnBuy64':'https://www.onbuy.com/gb/unlocked-64gb-apple-iphone-11-black~c12871~p14100500/',
        'Amazon128':'https://www.amazon.co.uk/Apple-MHDH3B-A-iPhone-128GB/dp/B08L6Z1M4Y/ref=sr_1_3?dchild=1&keywords=iphone+11+128gb&qid=1608814414&sr=8-33',
        'GiffGaff128':'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11/new',
        'Currys128':'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-11-128-gb-black-10197976-pdt.html',
        'Apple128':'https://www.apple.com/uk/shop/buy-iphone/iphone-11/6.1-inch-display-128gb-black',
        'JohnLewis128':'https://www.johnlewis.com/apple-iphone-11-ios-6-1-inch-4g-lte-sim-free-128gb/black/p4529033',
        'Argos128':'https://www.argos.co.uk/product/2072270?clickSR=slp:term:iphone%2011%20128gb:1:158:1',
        'OnBuy128':'https://www.onbuy.com/gb/apple-iphone-11-black~c12871~p14100493/',
        'ebay128':'https://www.ebay.co.uk/itm/New-Apple-iPhone-11-RED-128GB-Unlocked-A2221-CDMA-GSM-UK-Version/124360083272?epid=17034215590&hash=item1cf4704748:g:zCUAAOSwDNxfdSUu',

    }

    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r,'html.parser')

    def getListPrice_BrandNew(self):
        l = [
            self.getPrice_vendi_64gb(),
            self.getPrice_ebay_64gb(),
            self.getPrice_apple_64gb(),
            '£599',
            self.getPrice_johnlewis_64gb(),
            self.getPrice_currys_64gb(),
            '£599',
            '£599',
            self.getPrice_onbuy_64gb(),
            '£649',
            '£649',
            self.getPrice_currys_128gb(),
            self.getPrice_apple_128gb(),
            self.getPrice_johnlewis_128gb(),
            '£649',
            self.getPrice_onbuy_128gb(),
            self.getPrice_ebay_128gb(),
        ]
        try:
            return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', x)[0]), l))
        except:
            print("Error IPhone11")

    def getPrice_vendi_64gb(self):
        url = self.websites['vendi64']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[0].text.replace(',', '').split('£')[-1]
        else:
            return '£566'

    def getPrice_ebay_64gb(self):
        url = 'https://www.ebay.co.uk/itm/NEW-Apple-MWLT2B-A-iPhone-11-6-1-4G-Smartphone-64GB-Unlocked-Sim-Free-Black/352909507761?epid=22034217345&hash=item522b0bbcb1%3Ag%3Aq4UAAOSwE91d%7ELnh&LH_ItemCondition=1000'
        return self.get_soap(url).find('span',id = 'prcIsum').text

    def getPrice_apple_64gb(self):
        url = 'https://www.apple.com/uk/shop/buy-iphone/iphone-11'
        return self.get_soap(url).find_all('span', class_ = 'current_price')[0].text

    # No acсess html
    # def getPrice_giffGaff_64gb(self):
    #     url = 'https://www.giffgaff.com/mobile-phones/apple/apple-iphone-11/new'
    #     r = requests.get(url).text
    #     soap = BeautifulSoup(r, 'html.parser')
    #     print(r)

    def getPrice_johnlewis_64gb(self):
        url = 'https://www.johnlewis.com/apple-iphone-11-ios-6-1-inch-4g-lte-sim-free-64gb/green/p4519032'
        return self.get_soap(url).find('p', class_ = 'price price--large').text.replace(' ','').replace('\n','')

    def getPrice_currys_64gb(self):
        url = 'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-11-64-gb-black-10197974-pdt.html'
        return self.get_soap(url).find('strong', class_ = 'current').text

    def getPrice_onbuy_64gb(self):
        url = self.websites['OnBuy64']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    # No price
    # def getPrice_amazon_64gb(self):
    #     url = 'https://www.amazon.co.uk/Apple-MHDA3B-A-iPhone-Black/dp/B08L6YSCDF/ref=sr_1_3?dchild=1&keywords=iphone%2B11%2B64gb&qid=1608811569&sr=8-3&th=1'
    #     soap = self.get_soap(url)
    #     print(soap)

    def getPrice_onbuy_128gb(self):
        url = 'https://www.onbuy.com/gb/apple-iphone-11-black~c12871~p14100493/'
        return self.get_soap(url).find('div', class_ = 'price').text.replace(' ','').replace('\n','')

    def getPrice_currys_128gb(self):
        url = 'https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/apple-iphone-11-128-gb-black-10197976-pdt.html'
        return self.get_soap(url).find('strong', class_='current').text

    def getPrice_apple_128gb(self):
        url = 'https://www.apple.com/uk/shop/buy-iphone/iphone-11/6.1-inch-display-128gb-black'
        return self.get_soap(url).find_all('span', class_='current_price')[1].text

    def getPrice_johnlewis_128gb(self):
        url = 'https://www.johnlewis.com/apple-iphone-11-ios-6-1-inch-4g-lte-sim-free-128gb/black/p4529033'
        return self.get_soap(url).find('p', class_='price price--large').text.replace(' ','').replace('\n','')

    #The request takes a long time to complete
    # def getPrice_argos_128gb(self):
    #     url = 'https://www.argos.co.uk/product/2072270?clickSR=slp:term:iphone%2011%20128gb:1:158:1'
    #     r = requests.get(url)

    def getPrice_ebay_128gb(self):
        url = 'https://www.ebay.co.uk/itm/New-Apple-iPhone-11-RED-128GB-Unlocked-A2221-CDMA-GSM-UK-Version/124360083272?epid=17034215590&_trkparms=ispr%3D1&hash=item1cf4704748:g:zCUAAOSwDNxfdSUu&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkp2NA0WuhQytmt4dbStg00MVESG4ICL0lYubWr3c7skRLC1PWK2gXmGpSmB2ezwKgBL2b9ha1Yz8mL7N5lXK8er0YBSs73RMXcsFTG%252BXM8bNfLa7JqpY8ujbxbxe6Ljj4HgmQuGvEu0au4GcwMhSRPwmYqbALRVX4kWPNt9%252FJamKcwiDiB%252BfSctro%252FtKq5OBRFLnPUqSNeovS1oXDyzsNtxTDMgYRVddEFhmell6W7B8V%252FYnywYwgLUvEzOGW%252B0%252FhSqU7uIDKcgKlkU15AIi1SqjEae2dCj%252B%252BsZGwkuFl7hr57cpr7EqQz0ePiHNsCkcQ54JIy%252BzZM5zgqd1Z9JipWxxCB4UPfzWhn8%252FcSMYMU2LO0lVu5y6kN8QABduv47%252FC%252FFIxNE18CjTjwvPVFZH5kH4Bp9bND7RvUIXbpoczESO2rxmKWiOnboeDEtS6iSGnQfqZVJRdt7VoJlUPe4zLXr7K3JzAHqxKbJb0J4JElwgd45VumX7QbPhUTJgpTfXukzO842Ei8k%252FPQeOLL90%252F7ApCT68to73eE5EBnNfoiLQa5logqJ%252FFg8sqKZcWL3i1tsfloNXM44pzX6h1yMuIzWhTPtmnCj8POH1TW8Yo9vxYSDAX5btYifUGmaWliHYbaGrz4URU51cFi4OFYs2nDFwLTdOZw9YK%252BISiehE21v2PCwC%252BWdDkszIy%252BzSrdjxfpIYUHAUzBG8vE0r1r6hHwky%252B4TgDFapghi34%252FhPxCIAf0JoRHfEpRYCnpp%252FGggc5dDctRRDYVeQFqcZQlx4AzQ%253D%253D%7Ccksum%3A12436008327292085b18cf8b45b091c7e07d5a389cb9%7Campid%3APL_CLK%7Cclp%3A2334524'
        return self.get_soap(url).find('span',id = 'prcIsum').text.split(' ')[0]


    def getData_BrandNew(self):
        IPhones = []
        prices = self.getListPrice_BrandNew()
        colors = ['Black', 'Green', 'Purple', 'White', 'Red', 'Space Grey', 'Gold', 'Silver']
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone11',
                    'condition': 'Brand new',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]', list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones

    #RENEWED

    websites_r = {
        'vendi64': 'https://shop.vendiapp.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q=iphone+11+64gb',
        'GradeMobile64':'https://grademobile.co.uk/products/iphone-11-unlocked?_pos=1&_sid=431d3a783&_ss=r',
        'OnBuy64':'https://www.onbuy.com/gb/unlocked-64gb-apple-iphone-11-black~c12871~p14100500/?condition=refurbished',
        'HandTec64':'https://www.handtec.co.uk/products/apple-iphone-11-64gb-white-unlocked-refurbished-excellent?variant=32871923744829',
        'HandTec128':'https://www.handtec.co.uk/collections/refurbished-apple-iphone-11/products/apple-iphone-11-128gb-black-unlocked-refurbished-excellent?variant=31568377086013',
        'Amazon64':'https://www.amazon.co.uk/Apple-iPhone-64GB-Green-Renewed/dp/B082DN72G3',
        '4Gadgets64':'https://www.4gadgets.co.uk/mobile-phones/apple/iphone-11/red',
        'ebay64':'https://www.ebay.co.uk/itm/Apple-iPhone-11-64GB-128GB-256GB-Unlocked-Smartphone-All-Colours-A2221/293811777489?epid=22034217345&_trkparms=ispr%3D1&hash=item44688befd1%3Ag%3ASeIAAOSwavtfodNy&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkvjzWOStkxwnlDuxSI1PVVsHzLFWjlPcAv4XAp3nfFgX%252F9xto%252BB1wbwyP3avsSrJx8qzEoo5lQZd5pYBn3I3ynxf24Nb4eqB28S7T%252Fj1xDn9a6Yla3I9Ciu0Y3H%252FXEoOGLy6JFiw5FowaMDS%252FZrcT4MjNx%252BN0EcKPV8Jh1KVkii4wcMoRro8Ya0z313DP37EKPP2UgeN7vOYnWMEXxjJIJpbo0izqZMJ5I%252FpOlUOIy%252BDvG%252FWfjybhtOh47BpGF52R7mfeyrQasYuyvPkpIn%252B6xjWknABK4QQ%252Fbm1gypmM2CoEl52JNWDzgSykip%252BZ3Y4A6Mv7v14PPna1bjBLLzhdsbIjr%252FwPVvg8djpgqHHhJXS73CaVKo8F3bFr2%252BwFFb2ydDBuFzkLLRxLvHUh3xg2LNgj722vKw5vJrUxnWJSlfdAuIEbIBdMPdUs0OU%252BxfoC%252BlkaIVQyfPuBD%252F4YDCdrpEAjJzHiUADfk7YHG4bySsNZUpWkP6PqIlOwsW0hvq%252BBnzHLEsWT5mDWB8wou%252FN2QPZWPPq6BtEGS%252BYxIaH31oclDJY1zk3mM0CuFt2q0v0AS20LUQtJH7CQhnp1CeMaWGKccvhA0u70ebfRU3yISoSm%252FRR0M1Am9cI6GtKLW9JxhOOA6CJJ1AH0emfXXN7Or9Nj27UMTnKDuTUdyH8mLLFF50lweQu8Kqxjb3KPaVaXPyU8nHSAW2ipbh6C7O5rAv9U13dm0v8aMWfzY%252FX5k%252Fc6ypUbm4Yn5RHGQGcn%252BLvdH%252FrlMVS1pc8DToQgTVZFDQ%253D%253D%7Ccksum%3A293811777489cf732ea7b06e40af97ce96e2570c4e6e%7Campid%3APL_CLK%7Cclp%3A2334524&LH_ItemCondition=2500%7C2000',
        'BackMarket64':'https://www.backmarket.co.uk/second-hand-iphone-11-64-gb-black-unlocked/290057.html#?l=0',
        'GradeMobile128':'https://grademobile.co.uk/products/iphone-11-unlocked?variant=32025039339613',
        'Amazon128':'https://www.amazon.co.uk/Apple-iPhone-128GB-Black-Renewed/dp/B082BHJ9G8/ref=psdc_356496011_t3_B082BHW55H',
        'EnviroFone64':'https://shop.envirofone.com/buy/apple/iphone-11',
        'MusicMagpie64':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-64gb-black-unlocked',
        'ebay128':'https://www.ebay.co.uk/itm/Apple-iPhone-11-64GB-128GB-256GB-Unlocked-Smartphone-All-Colours-A2221/293811777489?epid=22034217345&_trkparms=ispr%3D1&hash=item44688befd1%3Ag%3ASeIAAOSwavtfodNy&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkvjzWOStkxwnlDuxSI1PVVsHzLFWjlPcAv4XAp3nfFgX%252F9xto%252BB1wbwyP3avsSrJx8qzEoo5lQZd5pYBn3I3ynxf24Nb4eqB28S7T%252Fj1xDn9a6Yla3I9Ciu0Y3H%252FXEoOGLy6JFiw5FowaMDS%252FZrcT4MjNx%252BN0EcKPV8Jh1KVkii4wcMoRro8Ya0z313DP37EKPP2UgeN7vOYnWMEXxjJIJpbo0izqZMJ5I%252FpOlUOIy%252BDvG%252FWfjybhtOh47BpGF52R7mfeyrQasYuyvPkpIn%252B6xjWknABK4QQ%252Fbm1gypmM2CoEl52JNWDzgSykip%252BZ3Y4A6Mv7v14PPna1bjBLLzhdsbIjr%252FwPVvg8djpgqHHhJXS73CaVKo8F3bFr2%252BwFFb2ydDBuFzkLLRxLvHUh3xg2LNgj722vKw5vJrUxnWJSlfdAuIEbIBdMPdUs0OU%252BxfoC%252BlkaIVQyfPuBD%252F4YDCdrpEAjJzHiUADfk7YHG4bySsNZUpWkP6PqIlOwsW0hvq%252BBnzHLEsWT5mDWB8wou%252FN2QPZWPPq6BtEGS%252BYxIaH31oclDJY1zk3mM0CuFt2q0v0AS20LUQtJH7CQhnp1CeMaWGKccvhA0u70ebfRU3yISoSm%252FRR0M1Am9cI6GtKLW9JxhOOA6CJJ1AH0emfXXN7Or9Nj27UMTnKDuTUdyH8mLLFF50lweQu8Kqxjb3KPaVaXPyU8nHSAW2ipbh6C7O5rAv9U13dm0v8aMWfzY%252FX5k%252Fc6ypUbm4Yn5RHGQGcn%252BLvdH%252FrlMVS1pc8DToQgTVZFDQ%253D%253D%7Ccksum%3A293811777489cf732ea7b06e40af97ce96e2570c4e6e%7Campid%3APL_CLK%7Cclp%3A2334524&LH_ItemCondition=2500%7C2000',
        'BackMarket128':'https://www.backmarket.co.uk/second-hand-iphone-11-128-gb-black-unlocked/290063.html#scroll=false',
        'MusicMagpie128':'https://www.musicmagpie.co.uk/store/products/apple-iphone-11-128gb-black-unlocked',
        'OnBuy128':'https://www.onbuy.com/gb/unlocked-128gb-apple-iphone-11-black~c12871~p14100509/',

    }

    def getPrice_vendi_64gb_r(self):
        url = self.websites['vendi64']
        if len(self.get_soap(url).find_all('span', class_='price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_='price')[1].text.replace(',', '').split('£')[-1]
        else:
            return '£472'

    def getPrice_GradeMobile_64gb_r(self):
        url = self.websites_r['GradeMobile64']
        return self.get_soap(url).find('span', class_ = 'product__price product__price--new h4').text

    def getPrice_OnBuy_64gb_r(self):
        url = self.websites_r['OnBuy64']
        return self.get_soap(url).find('div', class_ = 'price').text.replace(' ','').replace('\n','')

    def getPrice_HandTec_64gb_r(self):
        url = self.websites_r['HandTec64']
        return self.get_soap(url).find('span', id='ProductPrice').text

    def getPrice_HandTec_128gb_r(self):
        url = self.websites_r['HandTec128']
        return self.get_soap(url).find('span', id='ProductPrice').text

    #Block
    # def getPrice_Amazon_64gb_r(self):
    #     url = self.websites_r['Amazon64']
    #     return self.get_soap(url).find('span', class_ = 'a-size-medium a-color-price priceBlockBuyingPriceString')

    def getPrice_4Gadgets_64gb_r(self):
        url = self.websites_r['4Gadgets64']
        return '£'+self.get_soap(url).find_all('span',itemprop = 'price')[3].text

    def getPrice_ebay_64gb_r(self):
        url = self.websites_r['ebay64']
        return self.get_soap(url).find('span',id = 'prcIsum').text

    def getPrice_BackMarket_64gb_r(self):
        url = self.websites_r['BackMarket64']
        return self.get_soap(url).find('div', class_ = 'price primary large').text.replace(' ','').replace('\n','')

    def getPrice_GradeMobile_128gb_r(self):
        url = self.websites_r['GradeMobile128']
        return self.get_soap(url).find('span', class_='product__price product__price--new h4').text

    #Block
    # def getPrice_Amazon_128gb_r(self):
    #     url = self.websites_r['Amazon128']
    #     return self.get_soap(url).find('span',id = 'priceblock_ourprice')

    def getPrice_EnviroFone_64gb_r(self):
        url = self.websites_r['EnviroFone64']
        return self.get_soap(url).find('div', class_ = 'price-prod').text

    def getPrice_MusicMagpie_64gb_r(self):
        url = self.websites_r['MusicMagpie64']
        return self.get_soap(url).find('span', class_ = 'text-heavy xl-font').text

    def getPrice_ebay_128gb_r(self):
        url = self.websites_r['ebay128']
        # return self.get_soap(url).find('span',id = 'prcIsum').text
        return '£514.95'

    def getPrice_BackMarket_128gb_r(self):
        url = self.websites_r['BackMarket128']
        return self.get_soap(url).find('div', class_='price primary large').text.replace(' ', '').replace('\n', '')

    def getPrice_MusicMagpie_128gb_r(self):
        url = self.websites_r['MusicMagpie128']
        return self.get_soap(url).find('span', class_='text-heavy xl-font').text

    def getPrice_OnBuy_128gb_r(self):
        url = self.websites_r['OnBuy128']
        return self.get_soap(url).find('div', class_='price').text.replace(' ', '').replace('\n', '')

    def getListPrice_Renewed(self):
        l = []
        l.append(self.getPrice_vendi_64gb_r())
        l.append(self.getPrice_GradeMobile_64gb_r())
        l.append(self.getPrice_OnBuy_64gb_r())
        l.append(self.getPrice_HandTec_64gb_r())
        l.append(self.getPrice_HandTec_128gb_r())
        l.append('£492.45')
        l.append(self.getPrice_4Gadgets_64gb_r())
        l.append(self.getPrice_ebay_64gb_r())
        l.append(self.getPrice_BackMarket_64gb_r())
        l.append(self.getPrice_GradeMobile_128gb_r())
        l.append('£542.00')
        l.append(self.getPrice_EnviroFone_64gb_r())
        l.append(self.getPrice_MusicMagpie_64gb_r())
        l.append(self.getPrice_ebay_128gb_r())
        l.append(self.getPrice_BackMarket_128gb_r())
        l.append(self.getPrice_MusicMagpie_128gb_r())
        l.append(self.getPrice_OnBuy_128gb_r())
        return list(map(lambda x: float(re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', x)[0]), l))


    def getData_Renewed(self):
        IPhones = []
        prices = self.getListPrice_Renewed()
        colors = ['Black', 'Green', 'Purple', 'White', 'Red', 'Space Grey', 'Gold', 'Silver']
        for i in range(len(self.websites.keys())):
            data = {'brand': 'Apple',
                    'model': 'IPhone11',
                    'condition': 'Renewed',
                    'capacity': ''.join(re.findall(r'["64"|"128"|"256"|"512"]', list(self.websites.keys())[i])) + 'gb',
                    'retailerName': re.findall(r'\D+', list(self.websites.keys())[i])[0],
                    'priceInPounds': prices[i],
                    'colors': colors,
                    'url': list(self.websites.values())[i],
                    }

            IPhones.append(data)
        return IPhones



