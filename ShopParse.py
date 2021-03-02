import json, requests, re
from bs4 import BeautifulSoup

class ShopParse:

    @staticmethod
    def get_soap(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')

    def Vendi(self,url):
        if len(self.get_soap(url).find_all('span', class_ = 'price')) != 0:
            return '£' + self.get_soap(url).find_all('span', class_ = 'price')[0].text.replace(',','').split('£')[-1]
        #else:

    def _4Gadgets(self,url):
        pass

    def Amazon(self,url):
        pass

    def Apple(self,url):
        pass

    def Argos(self,url):
        pass

    def BackMarket(self,url):
        pass

    def CarphoneWarehouse(self,url):
        pass

    def CurrysPc(self,url):
        pass

    def Ebay(self,url):
        pass

    def Envirofone(self,url):
        pass

    def GiffGaff(self,url):
        pass

    def GradeMobile(self,url):
        pass

    def HandTec(self,url):
        pass

    def JohnLewis(self,url):
        pass

    def LaptopsDirect(self,url):
        pass

    def MusicMagpie(self,url):
        pass

    def OnBuy(self,url):
        pass

    def Smartfonestore(self,url):
        pass
    
































