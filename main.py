import json, requests, re, time
from bs4 import BeautifulSoup
from IPhone11 import IPhone11
from IPhone12pro import IPhone12pro
from IPhone12mini import IPhone12mini
from IPhone11proMax import IPhone11proMax
from IPhone12 import IPhone12
from IPhone12proMax import IPhone12proMax
from IPhone11pro import IPhone11pro
import Script_LiveUpdate


def main():
    Script_LiveUpdate.Update()
    Script_LiveUpdate.SellMyMobile_Price_Json()





if __name__ == '__main__':
    main()

