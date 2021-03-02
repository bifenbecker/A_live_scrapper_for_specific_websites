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
from multiprocessing import Process


def main():
    # while True:
    #     try:
    #         Script_LiveUpdate.Update()
    #         Script_LiveUpdate.SellMyMobile_Price_Json()
    #     except:
    #         print("Stop")
    #         break
    #     print("Succses")
    #     time.sleep(20)
    iphone11 = IPhone11()
    iphone12pro = IPhone12pro()
    iphone12mini = IPhone12mini()
    iphone11proMax = IPhone11proMax()
    iphone12 = IPhone12()
    iphone12proMax = IPhone12proMax()
    iphone11pro = IPhone11pro()

    data1 = iphone11.getData_BrandNew() + iphone11.getData_Renewed()
    data2 = iphone12pro.getData_BrandNew()
    data3 = iphone12mini.getData_BrandNew()
    data4 = iphone11proMax.getData_BrandNew() + iphone11proMax.getData_Renewed()
    data5 = iphone12.getData_BrandNew()
    data6 = iphone12proMax.getData_BrandNew()
    data7 = iphone11pro.getData_BrandNew() + iphone11pro.getData_Renewed()


if __name__ == '__main__':
    main()


